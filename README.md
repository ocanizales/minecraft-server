# bullet's Minecraft server

A small Fabric server for friends, built from mods on [Modrinth](https://modrinth.com).
It runs in Docker with [`itzg/minecraft-server`](https://docker-minecraft-server.readthedocs.io/),
which downloads the server mods itself on start.

- **Minecraft:** 1.21.1
- **Loader:** Fabric
- **Server address:** ask bullet

## Joining

1. Install the [Modrinth App](https://modrinth.com/app).
2. Create a profile: **Fabric**, **1.21.1**.
3. Add every mod in [Client mods](#client-mods) below. The Modrinth App adds
   their dependencies for you.
4. Play → Multiplayer → add the server address.

## Server mods

These run on the server, set in `MODRINTH_PROJECTS` in `docker-compose.yml`.

| Mod | Why it's on the server |
| --- | --- |
| [Fabric API](https://modrinth.com/mod/fabric-api) | Required by almost every Fabric mod |
| [Lithium](https://modrinth.com/mod/lithium) | Server tick performance; no gameplay change |
| [ModernFix](https://modrinth.com/mod/modernfix) | Lower memory use and faster start |
| [AppleSkin](https://modrinth.com/mod/appleskin) | Sends real saturation values to clients so the HUD is accurate |
| [VeinMiner](https://modrinth.com/mod/veinminer) | The vein-mining itself happens on the server |

Pulled in automatically: [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin) (VeinMiner).

## Client mods

Install these in your Modrinth App profile. Client-only mods are not on the
server and do not need to match anyone else's.

| Mod | Needed to join? | Notes |
| --- | --- | --- |
| [Fabric API](https://modrinth.com/mod/fabric-api) | **Yes** | |
| [VeinMiner](https://modrinth.com/mod/veinminer) | **Yes** | Must match the server |
| [VeinMiner Hotkey](https://modrinth.com/mod/veinminer-client) | **Yes** | Hold a key to vein-mine; needs VeinMiner + Fabric Language Kotlin |
| [Sodium](https://modrinth.com/mod/sodium) | No | Rendering performance |
| [Lithium](https://modrinth.com/mod/lithium) | No | Helps singleplayer; harmless on a server |
| [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) | No | HUD/text rendering performance |
| [ModernFix](https://modrinth.com/mod/modernfix) | No | Memory and launch time |
| [Iris](https://modrinth.com/mod/iris) | No | Shader loader, required for Eclipse |
| [Eclipse](https://modrinth.com/shader/eclipseshaders) | No | Shader pack, see notes below |
| [Mod Menu](https://modrinth.com/mod/modmenu) | No | Mod list + config screens |
| [Falling Leaves](https://modrinth.com/mod/fallingleaves) | No | Needs Cloth Config |
| [Particle Rain](https://modrinth.com/mod/particle-rain) | No | Rain and snow particles |
| [Not Enough Animations](https://modrinth.com/mod/not-enough-animations) | No | Third-person animations |
| [AFK Cinematics](https://modrinth.com/mod/afk-cinematics) | No | Camera orbit when idle |
| [AppleSkin](https://modrinth.com/mod/appleskin) | No | Food and saturation HUD |
| [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) | No | |
| [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) | No | |
| [Just Enough Items](https://modrinth.com/mod/jei) | No | Recipe viewer |

Dependencies the Modrinth App adds for you: Cloth Config (Falling Leaves),
Placeholder API (Mod Menu), Fabric Language Kotlin (VeinMiner).

## Why 1.21.1

Checked against Modrinth on 2026-10-13.

| Version | Requested mods with a Fabric release | Fabric mods on Modrinth |
| --- | --- | --- |
| 26.3 (newest) | Missing AFK Cinematics, ModernFix, JEI | ~7,400 |
| 26.2 | Missing ModernFix | ~12,900 |
| 1.21.11 | Missing ModernFix | ~17,900 |
| **1.21.1** | **All of them** | **~19,500 (the most)** |

1.21.1 is the only version that runs the whole list, and it has the most
Fabric mods on Modrinth, so mods added later are most likely to have a build
for it. Most of these mods were still publishing 1.21.1 builds in 2026.

The cost: 1.21.1 doesn't have the 1.21.2–1.21.11 content (the bundle, the
pale garden, and so on). Dropping ModernFix (see below) would allow 1.21.11.

## Not included

- **Keybind Atlas:** Forge/NeoForge only, with no Fabric build for any
  version. The closest Fabric option is [Controlling](https://modrinth.com/mod/controlling),
  which adds search to the controls screen.

## Notes on the list

- **ModernFix:** it was built for large Forge modpacks and does little for a
  small Fabric pack. It is also the only reason the server is held at 1.21.1
  instead of 1.21.11, because its Fabric builds stopped at 1.21.1. If you'd
  rather have newer Minecraft than more mods, remove it.
- **Eclipse shaders:** it's a single beta release, listed for 1.21.5–1.21.8
  only. It may work on 1.21.1 under Iris, but that hasn't been tested. If it
  doesn't, [Complementary Reimagined](https://modrinth.com/shader/complementary-reimagined)
  and [BSL](https://modrinth.com/shader/bsl-shaders) both support 1.21.1.
  Shaders are the heaviest item on this list for a player's GPU.
- **Cinematic AFK:** two similar mods exist, [AFK Cinematics](https://modrinth.com/mod/afk-cinematics)
  (listed above) and [Ji AFK Cinematic](https://modrinth.com/mod/ji-afk-cinematic).
  Use one, not both.
- **Particle Rain:** none of the other mods add weather particles, so it
  doesn't overlap with anything.
- **JEI:** works on Fabric, but [EMI](https://modrinth.com/mod/emi) is the
  Fabric-native recipe viewer. Use one or the other, not both.

## Recommendations (not added)

Server:

- [Chunky](https://modrinth.com/mod/chunky): pre-generate the world once so
  exploring doesn't spike CPU on a shared VPS. Recommended first.
- [spark](https://modrinth.com/mod/spark): profiler for finding lag.
- [FerriteCore](https://modrinth.com/mod/ferrite-core): lower memory use;
  works on both server and client.
- [C2ME](https://modrinth.com/mod/c2me-fabric): faster chunk generation. It's
  an alpha release, so add it only if chunk generation turns out to be the
  bottleneck.
- [Simple Voice Chat](https://modrinth.com/mod/simple-voice-chat): proximity
  voice chat. Needs an extra UDP port (24454) open.

Client:

- [Entity Culling](https://modrinth.com/mod/entityculling) and
  [Dynamic FPS](https://modrinth.com/mod/dynamic-fps): more performance, and
  they pair well with Sodium.
- [Sodium Extra](https://modrinth.com/mod/sodium-extra) and
  [Reese's Sodium Options](https://modrinth.com/mod/reeses-sodium-options):
  more video settings.
- [Jade](https://modrinth.com/mod/jade): shows what you're looking at.
- [Mouse Tweaks](https://modrinth.com/mod/mouse-tweaks): faster inventory
  handling.
- [Controlling](https://modrinth.com/mod/controlling): replacement for
  Keybind Atlas.

## Running it

```sh
cp .env.example .env        # set RCON_PASSWORD
docker compose up -d        # start
docker compose logs -f      # watch it start up
docker compose down         # stop
```

**To add a server mod:** add its Modrinth slug (the part after
`modrinth.com/mod/`) to `MODRINTH_PROJECTS`, run `docker compose up -d`, and
add the mod to the tables above.

`data/` holds the world and runtime files and is not committed.
