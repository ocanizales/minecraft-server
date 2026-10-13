# bullet's Minecraft server

A small Fabric server for friends, built from mods on [Modrinth](https://modrinth.com).
The main gameplay is **Tensura: Reincarnated** (That Time I Got Reincarnated
as a Slime): pick a race, earn skills, and go the True Hero or Demon Lord
route. It runs in Docker with [`itzg/minecraft-server`](https://docker-minecraft-server.readthedocs.io/),
which downloads the server mods itself on start.

- **Minecraft:** 1.21.1
- **Loader:** Fabric
- **Server address:** ask bullet

## Joining

1. Install the [Modrinth App](https://modrinth.com/app).
2. Create a profile: **Fabric**, **1.21.1**.
3. Add every mod in [Client mods](#client-mods) below, **including the
   Tensura libraries**. The Modrinth App adds most dependencies for you, but
   not Tensura's (see [Tensura libraries](#tensura-libraries)).
4. Play → Multiplayer → add the server address.

## Server mods

These run on the server, set in `MODRINTH_PROJECTS` in `docker-compose.yml`.

| Mod | Why it's on the server |
| --- | --- |
| [Fabric API](https://modrinth.com/mod/fabric-api) | Required by almost every Fabric mod |
| [Tensura: Reincarnated](https://modrinth.com/mod/tensura-reincarnated) | The main gameplay: races, skills, magic, bosses, Tensura civilizations |
| [Tensura: Mysticism](https://modrinth.com/mod/tensura-mysticism) | Add-on: more magic, skills and content |
| [Tensura: Not Enough Bosses](https://modrinth.com/mod/tensura-not-enough-bosses) | Official add-on: more bosses |
| [Tensura: SlimeThrone Extras](https://modrinth.com/mod/tensura-slimethrone-extras) | Add-on: more races, skills and items |
| [Tensura: Better Subordinates](https://modrinth.com/mod/tensura-better-subordinates) | Add-on: train subordinates and teach them skills |
| [MCA Reborn](https://modrinth.com/mod/minecraft-comes-alive-reborn) | Villager overhaul: real villagers you can talk to, befriend and marry |
| [Lithium](https://modrinth.com/mod/lithium) | Server tick performance; no gameplay change |
| [Chunky](https://modrinth.com/mod/chunky) | Pre-generates the world so exploring doesn't spike the CPU (see below) |
| [Tree Harvester](https://modrinth.com/mod/tree-harvester) | Chop one log with an axe and the whole tree (or huge mushroom) comes down, with fast leaf decay and sapling replanting |
| [AppleSkin](https://modrinth.com/mod/appleskin) | Sends real saturation values to clients so the HUD is accurate |
| [VeinMiner](https://modrinth.com/mod/veinminer) | The vein-mining itself happens on the server |

Also listed in compose: the five [Tensura libraries](#tensura-libraries).
Pulled in automatically: [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin) (VeinMiner)
and [Collective](https://modrinth.com/mod/collective) (Tree Harvester; a shared code library for
Serilum's mods that adds nothing on its own).

## Tensura libraries

Tensura's mod files require these libraries, but its Modrinth pages don't
list them, so neither the server nor the Modrinth App adds them on its own.
Without them the game refuses to start. **Install all five yourself:**

- [Architectury API](https://modrinth.com/mod/architectury-api)
- [GeckoLib](https://modrinth.com/mod/geckolib)
- [SmartBrainLib](https://modrinth.com/mod/smartbrainlib) (its page says
  "server only", but Tensura needs it on the client too)
- [TerraBlender](https://modrinth.com/mod/terrablender)
- [ManasCore](https://modrinth.com/mod/manascore)

## Client mods

Install these in your Modrinth App profile, plus the five libraries above.
Client-only mods are not on the server and do not need to match anyone else's.

| Mod | Needed to join? | Notes |
| --- | --- | --- |
| [Fabric API](https://modrinth.com/mod/fabric-api) | **Yes** | |
| [Tensura: Reincarnated](https://modrinth.com/mod/tensura-reincarnated) | **Yes** | Must match the server |
| [Tensura: Mysticism](https://modrinth.com/mod/tensura-mysticism) | **Yes** | |
| [Tensura: Not Enough Bosses](https://modrinth.com/mod/tensura-not-enough-bosses) | **Yes** | |
| [Tensura: SlimeThrone Extras](https://modrinth.com/mod/tensura-slimethrone-extras) | **Yes** | |
| [Tensura: Better Subordinates](https://modrinth.com/mod/tensura-better-subordinates) | **Yes** | |
| [MCA Reborn](https://modrinth.com/mod/minecraft-comes-alive-reborn) | **Yes** | |
| [VeinMiner](https://modrinth.com/mod/veinminer) | **Yes** | Must match the server |
| [VeinMiner Hotkey](https://modrinth.com/mod/veinminer-client) | **Yes** | Hold a key to vein-mine; needs VeinMiner + Fabric Language Kotlin |
| [Tensura Voice](https://modrinth.com/mod/tensura-voice) | No | Voice of the World animations and sounds |
| [Sodium](https://modrinth.com/mod/sodium) | No | Rendering performance |
| [Iris](https://modrinth.com/mod/iris) | No | Shader loader. **Pick version 1.8.14-beta.1**, see notes |
| [Eclipse](https://modrinth.com/shader/eclipseshaders) | No | Shader pack, see notes below |
| [Lithium](https://modrinth.com/mod/lithium) | No | Helps singleplayer; harmless on a server |
| [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) | No | HUD/text rendering performance |
| [Mod Menu](https://modrinth.com/mod/modmenu) | No | Mod list + config screens |
| [Falling Leaves](https://modrinth.com/mod/fallingleaves) | No | Needs Cloth Config |
| [Particle Rain](https://modrinth.com/mod/particle-rain) | No | Rain and snow particles |
| [Not Enough Animations](https://modrinth.com/mod/not-enough-animations) | No | Third-person animations |
| [AFK Cinematics](https://modrinth.com/mod/afk-cinematics) | No | Camera orbit when idle |
| [AppleSkin](https://modrinth.com/mod/appleskin) | No | Food and saturation HUD |
| [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) | No | |
| [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) | No | |
| [Just Enough Items](https://modrinth.com/mod/jei) | No | Recipe viewer |
| [Dynamic FPS](https://modrinth.com/mod/dynamic-fps) | No | Lowers frame rate and volume when the game is in the background, idle or on battery |
| [Visuality](https://modrinth.com/mod/visuality) | No | Extra particles: mob hits, slime blobs, crystal sparkles, ambient effects; needs Cloth Config |
| [Spatial GUI](https://modrinth.com/mod/spatial-gui) | No | Draws inventory and container screens as a 3D panel instead of a flat overlay; needs Mod Menu + Cloth Config |

Dependencies the Modrinth App adds for you: Cloth Config (Falling Leaves,
Visuality, Spatial GUI), Placeholder API (Mod Menu), Fabric Language Kotlin (VeinMiner).
Tree Harvester is server-only, so players don't install it.

## Why 1.21.1

Tensura: Reincarnated and every Tensura add-on only go up to 1.21.1, so the
server can't be newer than that while Tensura is the main gameplay. Every
other mod on the list also has a Fabric 1.21.1 release (checked 2026-10-13),
and 1.21.1 has the most Fabric mods on Modrinth (~19,500), so later
additions are likely to have a build.

The server briefly ran 1.21.11 before Tensura was added. Going back costs
the 1.21.2–1.21.11 vanilla content (the bundle, the pale garden, and so on).

## Taken from the TenSura modpack

The Tensura mods come from Kesselot's
[TenSura modpack](https://modrinth.com/modpack/tensura-suraimu) (3.1.2,
NeoForge 1.21.1), keeping only the main gameplay. These parts of the pack
are **NeoForge-only**, so they can't run on this Fabric server:

- Tensura add-ons bundled in the pack: Ascension, Great Sage, Gear Evolution,
  Fox Ablaze Ultimate, Tensura Guild, Unique Monsters, backpack tiers
- MineColonies, Sophisticated Backpacks, Cosmetic Armor Reworked

## Not included

- **Keybind Atlas:** Forge/NeoForge only, with no Fabric build for any
  version. The closest Fabric option is [Controlling](https://modrinth.com/mod/controlling),
  which adds search to the controls screen.
- **ModernFix:** dropped. It was built for large Forge modpacks and does
  little for a Fabric pack.

## Notes on the list

- **Iris and Sodium:** the newest Sodium for 1.21.1 (0.8.13) refuses to load
  with Iris older than 1.8.13, and the newest *release* of Iris for 1.21.1 is
  1.8.8. Install **Iris 1.8.14-beta.1**, the pairing the TenSura modpack
  itself ships. In the Modrinth App, open Iris's versions and pick it by hand.
- **Chunky:** it does nothing until it's told to. After the first start,
  run it once from the console, for example
  `docker exec minecraft rcon-cli chunky radius 2000` and then
  `docker exec minecraft rcon-cli chunky start`. It can be paused and resumed,
  and the size can be changed.
- **Tree Harvester + VeinMiner:** VeinMiner can also break whole veins of
  logs. If both would trigger on the same tree, turn logs off in VeinMiner.
- **Eclipse shaders:** it's a single beta release, listed for 1.21.5–1.21.8
  only. Shader packs often keep working across versions under Iris, but that
  hasn't been tested on 1.21.1. If it doesn't work,
  [Complementary Reimagined](https://modrinth.com/shader/complementary-reimagined)
  and [BSL](https://modrinth.com/shader/bsl-shaders) both support 1.21.1.
  Shaders are the heaviest item on this list for a player's GPU.
- **Cinematic AFK:** two similar mods exist, [AFK Cinematics](https://modrinth.com/mod/afk-cinematics)
  (listed above) and [Ji AFK Cinematic](https://modrinth.com/mod/ji-afk-cinematic).
  Use one, not both.
- **Particle Rain:** none of the other mods add weather particles, so it
  doesn't overlap with anything.

## Recommendations (not added)

Server:

- [Serene Seasons](https://modrinth.com/mod/serene-seasons): real seasons.
  Grass and leaves change color, it snows in winter, and crops only grow in
  their seasons, which makes farming much harder. It's in the TenSura pack
  and has a Fabric 1.21.1 build. Needed on both server and client.
- [spark](https://modrinth.com/mod/spark): profiler for finding lag.
- [FerriteCore](https://modrinth.com/mod/ferrite-core): lower memory use;
  works on both server and client.
- [C2ME](https://modrinth.com/mod/c2me-fabric): faster chunk generation,
  which also makes Chunky faster. Only an alpha exists for 1.21.1.
- [Simple Voice Chat](https://modrinth.com/mod/simple-voice-chat): proximity
  voice chat. Needs an extra UDP port (24454) open.

Client:

- [Entity Culling](https://modrinth.com/mod/entityculling): skips drawing
  mobs and block entities you can't see; pairs well with Sodium.
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
add the mod to the tables above. Check that the mod file's own dependencies
are covered, not just the ones on its Modrinth page. Tensura is the example
of why.

`data/` holds the world and runtime files and is not committed.
