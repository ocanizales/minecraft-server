#!/usr/bin/env python3
"""Announce a mod change in the in-game chat, through RCON.

Usage:
  python3 pack/announce.py profile "Added Inventory Profiles Next (take-all button on chests)"
  python3 pack/announce.py server  "Added ServerCore"
  python3 pack/announce.py restart "Restarting in 30 seconds to add new mods"

  profile = players must download the new profile to get it
  server  = server-side only; nothing to download
  restart = warning before a restart (no download link)

Only players online at that moment see it. Stdlib only.
"""
import json
import subprocess
import sys

DOWNLOAD = "https://github.com/ocanizales/minecraft-server/releases/latest/download/bullets-server.mrpack"
FOLLOW_UP = {
    "profile": "Re-download the modpack and import it to get this:",
    "server": "Server-side only, nothing to download. Rejoin if you don't see it.",
    "restart": "",
}


def tellraw(parts):
    cmd = "tellraw @a " + json.dumps(parts)
    subprocess.run(["docker", "exec", "minecraft", "rcon-cli", cmd], check=True)


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in FOLLOW_UP:
        sys.exit(__doc__)
    kind, message = sys.argv[1], sys.argv[2]
    tellraw([
        {"text": "[Server] ", "color": "gold", "bold": True},
        {"text": message, "color": "yellow", "bold": False},
    ])
    if FOLLOW_UP[kind]:
        line = [{"text": FOLLOW_UP[kind] + " ", "color": "gray"}]
        if kind == "profile":
            line.append({
                "text": "[Download modpack]",
                "color": "aqua",
                "underlined": True,
                "clickEvent": {"action": "open_url", "value": DOWNLOAD},
                "hoverEvent": {"action": "show_text", "contents": "Opens the newest player profile (.mrpack)"},
            })
        tellraw(line)


if __name__ == "__main__":
    main()
