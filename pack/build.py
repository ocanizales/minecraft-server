#!/usr/bin/env python3
"""Resolve pack/mods.toml against Modrinth, then:

- rewrite MODRINTH_PROJECTS in docker-compose.yml with exact version IDs, so
  the server runs the same builds as the player profile;
- build dist/bullets-server.mrpack, the profile players import into the
  Modrinth App.

Every jar's fabric.mod.json `depends` is checked against the whole set,
because some mods (Tensura) need libraries their Modrinth pages never declare.

Usage: python3 pack/build.py <pack-version>     e.g. 2026.10.13
Stdlib only.
"""
import hashlib
import io
import json
import re
import sys
import tomllib
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.modrinth.com/v2"
UA = "ocanizales/minecraft-server (github.com/ocanizales/minecraft-server)"
CACHE = ROOT / "dist" / "cache"
PACK_NAME = "bullet's server"
# Provided by the loader or the game itself, never by a mod on the list.
BUILTIN = {"minecraft", "java", "fabricloader", "fabric", "mixinextras"}


def get(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read() if raw else json.load(r)


def pick_version(slug, mc, ptype, pinned):
    loader = "iris" if ptype == "shader" else "fabric"
    query = urllib.parse.urlencode({"loaders": f'["{loader}"]', "game_versions": f'["{mc}"]'})
    versions = get(f"{API}/project/{slug}/version?{query}")
    if pinned:
        match = [v for v in versions if v["version_number"] == pinned]
        if not match:
            sys.exit(f"{slug}: pinned version {pinned} not found for {loader} {mc}")
        return match[0]
    releases = [v for v in versions if v["version_type"] == "release"]
    if not releases:
        sys.exit(f"{slug}: no {loader} release for {mc}")
    return releases[0]


def jar_bytes(file):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / file["filename"]
    if not path.exists():
        path.write_bytes(get(file["url"], raw=True))
    data = path.read_bytes()
    if hashlib.sha512(data).hexdigest() != file["hashes"]["sha512"]:
        path.unlink()
        sys.exit(f"hash mismatch for {file['filename']}")
    return data


def mod_jsons(data):
    """fabric.mod.json of a jar and of every jar nested inside it."""
    jar = zipfile.ZipFile(io.BytesIO(data))
    if "fabric.mod.json" not in jar.namelist():
        return []
    # Some mods put raw newlines inside JSON strings; strict=False accepts them.
    meta = json.loads(jar.read("fabric.mod.json").decode("utf-8", "replace"), strict=False)
    found = [meta]
    for nested in meta.get("jars", []):
        try:
            found += mod_jsons(jar.read(nested["file"]))
        except KeyError:
            pass
    return found


def resolve(cfg):
    mc = cfg["minecraft"]
    wanted = {}
    for slug, spec in cfg["mods"].items():
        spec = {"side": spec} if isinstance(spec, str) else spec
        wanted[slug] = spec

    resolved = {}  # project id -> entry
    queue = [(slug, spec["side"], spec.get("version"), spec.get("minecraft", mc)) for slug, spec in wanted.items()]
    while queue:
        slug, side, pinned, listed_for = queue.pop(0)
        project = get(f"{API}/project/{slug}")
        entry = resolved.get(project["id"])
        if entry:
            entry["sides"].add(side)
            continue
        version = pick_version(project["slug"], listed_for, project["project_type"], pinned)
        resolved[project["id"]] = entry = {
            "slug": project["slug"],
            "type": project["project_type"],
            "version": version,
            "sides": {side},
        }
        for dep in version["dependencies"]:
            if dep["dependency_type"] == "required" and dep.get("project_id"):
                queue.append((dep["project_id"], side, None, mc))

    # Sides propagate to dependencies only one level per pass; repeat until stable.
    changed = True
    while changed:
        changed = False
        for entry in resolved.values():
            for dep in entry["version"]["dependencies"]:
                child = resolved.get(dep.get("project_id"))
                if dep["dependency_type"] == "required" and child and not entry["sides"] <= child["sides"]:
                    child["sides"] |= entry["sides"]
                    changed = True
    return resolved


def check_depends(resolved):
    provided, metas = set(BUILTIN), []
    for entry in resolved.values():
        if entry["type"] != "mod":
            continue
        file = primary(entry["version"])
        for meta in mod_jsons(jar_bytes(file)):
            provided.add(meta["id"])
            provided.update(meta.get("provides", []))
            metas.append((entry["slug"], meta))
    missing = [
        f"{slug} ({meta['id']}) needs {dep}"
        for slug, meta in metas
        for dep in (meta.get("depends") or {})
        if dep not in provided
    ]
    if missing:
        sys.exit("missing dependencies:\n  " + "\n  ".join(missing))


def primary(version):
    return next((f for f in version["files"] if f["primary"]), version["files"][0])


def on_server(entry):
    return bool(entry["sides"] & {"both", "server"})


def on_client(entry):
    return bool(entry["sides"] & {"both", "client"})


def write_compose(cfg, resolved):
    path = ROOT / "docker-compose.yml"
    text = path.read_text()
    for key, value in (("VERSION", cfg["minecraft"]), ("FABRIC_LOADER_VERSION", cfg["fabric_loader"])):
        text, n = re.subn(rf'(?m)^(      {key}: ).*$', rf'\g<1>"{value}"', text)
        if n != 1:
            sys.exit(f"{key} not found in docker-compose.yml")
    lines = sorted(
        f"        {e['slug']}:{e['version']['id']}"
        for e in resolved.values()
        if on_server(e) and e["type"] == "mod"
    )
    block = "      MODRINTH_PROJECTS: |-\n" + "\n".join(lines) + "\n"
    new, n = re.subn(r"      MODRINTH_PROJECTS: \|-\n(?:        .*\n)+", block, text)
    if n != 1:
        sys.exit("MODRINTH_PROJECTS block not found in docker-compose.yml")
    path.write_text(new)


def write_mrpack(cfg, resolved, pack_version):
    files = []
    for e in sorted(resolved.values(), key=lambda e: e["slug"]):
        if not on_client(e):
            continue
        file = primary(e["version"])
        folder = "shaderpacks" if e["type"] == "shader" else "mods"
        files.append({
            "path": f"{folder}/{file['filename']}",
            "hashes": {"sha1": file["hashes"]["sha1"], "sha512": file["hashes"]["sha512"]},
            "env": {"client": "required", "server": "required" if on_server(e) else "unsupported"},
            "downloads": [file["url"]],
            "fileSize": file["size"],
        })
    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": pack_version,
        "name": PACK_NAME,
        "summary": "Player profile for bullet's Tensura server",
        "files": files,
        "dependencies": {"minecraft": cfg["minecraft"], "fabric-loader": cfg["fabric_loader"]},
    }
    out = ROOT / "dist" / "bullets-server.mrpack"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("modrinth.index.json", json.dumps(index, indent=2))
    return out, len(files)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cfg = tomllib.loads((ROOT / "pack" / "mods.toml").read_text())
    resolved = resolve(cfg)
    check_depends(resolved)
    write_compose(cfg, resolved)
    out, count = write_mrpack(cfg, resolved, sys.argv[1])
    for e in sorted(resolved.values(), key=lambda e: e["slug"]):
        where = "+".join(s for s, ok in (("server", on_server(e)), ("client", on_client(e))) if ok)
        print(f"{e['slug']:32} {e['version']['version_number']:36} {where}")
    print(f"\n{out.relative_to(ROOT)}: {count} files; docker-compose.yml pinned")


if __name__ == "__main__":
    main()
