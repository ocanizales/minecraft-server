# bullet's Minecraft server

A small Fabric server for friends, built from mods on [Modrinth](https://modrinth.com).
It runs in Docker with [`itzg/minecraft-server`](https://docker-minecraft-server.readthedocs.io/),
which downloads the server mods itself on start.

- **Minecraft:** 1.21.11
- **Loader:** Fabric
- **Server address:** ask bullet

## Joining

1. Install the [Modrinth App](https://modrinth.com/app).
2. Create a profile: **Fabric**, **1.21.11**.
3. Add every mod in [Client mods](#client-mods) below. The Modrinth App adds
   their dependencies for you.
4. Play → Multiplayer → add the server address.

## Server mods

These run on the server, set in `MODRINTH_PROJECTS` in `docker-compose.yml`.

| Mod | Why it's on the server |
| --- | --- |
| [Fabric API](https://modrinth.com/mod/fabric-api) | Required by almost every Fabric mod |
| [Lithium](https://modrinth.com/mod/lithium) | Server tick performance; no gameplay change |
| [Chunky](https://modrinth.com/mod/chunky) | Pre-generates the world so exploring doesn't spike the CPU (see below) |
| [Tree Harvester](https://modrinth.com/mod/tree-harvester) | Chop one log with an axe and the whole tree (or huge mushroom) comes down, with fast leaf decay and sapling replanting |
| [AppleSkin](https://modrinth.com/mod/appleskin) | Sends real saturation values to clients so the HUD is accurate |
| [VeinMiner](https://modrinth.com/mod/veinminer) | The vein-mining itself happens on the server |

Pulled in automatically: [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin) (VeinMiner)
and [Collective](https://modrinth.com/mod/collective) (Tree Harvester; a shared code library for
Serilum's mods that adds nothing on its own).

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
| [Spatial GUI](https://modrinth.com/mod/spatial-gui) | No | Draws inventory and container screens as a 3D panel instead of a flat overlay; needs Mod Menu + Cloth Config |

Dependencies the Modrinth App adds for you: Cloth Config (Falling Leaves,
Spatial GUI), Placeholder API (Mod Menu), Fabric Language Kotlin (VeinMiner).
Tree Harvester is server-only, so players don't install it.

## Why 1.21.11

Checked against Modrinth on 2026-10-13.

| Version | Mods on the list with a Fabric release | Fabric mods on Modrinth |
| --- | --- | --- |
| 26.3 (newest) | Missing AFK Cinematics and JEI | ~7,400 |
| 26.2 | All of them | ~12,900 |
| **1.21.11** | **All of them** | **~17,900** |
| 1.21.1 | All of them | ~19,500 |

The server started on 1.21.1 only because ModernFix's Fabric builds end
there. With ModernFix dropped, 1.21.11 is the newest version that still has
the second-largest Fabric library on Modrinth. It's also the last 1.21
release, which gets far more mod support than the newer 26.x versions.

## Not included

- **Keybind Atlas:** Forge/NeoForge only, with no Fabric build for any
  version. The closest Fabric option is [Controlling](https://modrinth.com/mod/controlling),
  which adds search to the controls screen.
- **ModernFix:** dropped. It was built for large Forge modpacks, and its
  Fabric builds stop at 1.21.1.

## Notes on the list

- **Chunky:** it does nothing until it's told to. After the first start,
  run it once from the console, for example
  `docker exec minecraft rcon-cli chunky radius 2000` and then
  `docker exec minecraft rcon-cli chunky start`. It can be paused and resumed,
  and the size can be changed.
- **Tree Harvester + VeinMiner:** VeinMiner can also break whole veins of
  logs. If both would trigger on the same tree, turn logs off in VeinMiner.
- **Eclipse shaders:** it's a single beta release, listed for 1.21.5–1.21.8
  only. Shader packs often keep working across versions under Iris, but that
  hasn't been tested on 1.21.11. If it doesn't work,
  [Complementary Reimagined](https://modrinth.com/shader/complementary-reimagined)
  and [BSL](https://modrinth.com/shader/bsl-shaders) both support 1.21.11.
  Shaders are the heaviest item on this list for a player's GPU.
- **Cinematic AFK:** two similar mods exist, [AFK Cinematics](https://modrinth.com/mod/afk-cinematics)
  (listed above) and [Ji AFK Cinematic](https://modrinth.com/mod/ji-afk-cinematic).
  Use one, not both.
- **Particle Rain:** none of the other mods add weather particles, so it
  doesn't overlap with anything.

## Recommendations (not added)

Server:

- [spark](https://modrinth.com/mod/spark): profiler for finding lag.
- [FerriteCore](https://modrinth.com/mod/ferrite-core): lower memory use;
  works on both server and client.
- [C2ME](https://modrinth.com/mod/c2me-fabric): faster chunk generation,
  which also makes Chunky's pre-generation faster.
- [Simple Voice Chat](https://modrinth.com/mod/simple-voice-chat): proximity
  voice chat. Needs an extra UDP port (24454) open.

Client:

- [Entity Culling](https://modrinth.com/mod/entityculling): skips drawing
  mobs and block entities you can't see; pairs well with Sodium.
- [Dynamic FPS](https://modrinth.com/mod/dynamic-fps): lowers the frame
  rate and volume when Minecraft is in the background, idle or on battery.
  Saves GPU, heat and laptop battery; does nothing for in-game FPS or the
  server.
- [Visuality](https://modrinth.com/mod/visuality): extra cosmetic particles
  (hit particles, slime blobs, crystal sparkles, ambient effects).
  Overlaps in spirit with Particle Rain and Falling Leaves but not in what
  it adds.
- [Sodium Extra](https://modrinth.com/mod/sodium-extra) and
  [Reese's Sodium Options](https://modrinth.com/mod/reeses-sodium-options):
  more video settings.
- [Jade](https://modrinth.com/mod/jade): shows what you're looking at.
- [Mouse Tweaks](https://modrinth.com/mod/mouse-tweaks): faster inventory
  handling.
- [Controlling](https://modrinth.com/mod/controlling): replacement for
  Keybind Atlas (needs Searchables).

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
