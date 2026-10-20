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

[![Download the player profile](https://img.shields.io/badge/Modrinth_App-Download_player_profile-1bd96a?style=for-the-badge&logo=modrinth&logoColor=white)](https://github.com/ocanizales/minecraft-server/releases/latest/download/bullets-server.mrpack)

1. Install the [Modrinth App](https://modrinth.com/app).
2. Click the button above. It downloads `bullets-server.mrpack`, a ready-made
   Fabric 1.21.1 profile with every mod below, already at the exact versions
   the server runs.
3. Open the file. Double-clicking it opens it in the Modrinth App, or use
   **+ → Import from file** in the app.
4. Play → Multiplayer → add the server address.

When the mod list changes, a new profile is released at the same link.
Download it again and import it to update.

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
| [ServerCore](https://modrinth.com/mod/servercore) | Server optimizations: lowers view distance under load, slows ticking of far-away mobs, cheaper chunk ticks |
| [FTB Quests](https://www.curseforge.com/minecraft/mc-mods/ftb-quests-fabric) | Quest book. Comes empty; quests are written in-game by an op. Needs FTB Library and FTB Teams. CurseForge only |
| [Chunky](https://modrinth.com/mod/chunky) | Pre-generates the world so exploring doesn't spike the CPU (see below) |
| [Tree Harvester](https://modrinth.com/mod/tree-harvester) | Chop one log with an axe and the whole tree (or huge mushroom) comes down, with fast leaf decay and sapling replanting |
| [AppleSkin](https://modrinth.com/mod/appleskin) | Sends real saturation values to clients so the HUD is accurate |
| [VeinMiner](https://modrinth.com/mod/veinminer) | The vein-mining itself happens on the server |
| [Better Inventory and Backpacks](https://www.curseforge.com/minecraft/mc-mods/better-inventory-and-backpacks) | New inventory screen, wearable backpacks with upgrades (magnet, auto-feed, hotbar refill), sorting, bigger stacks in backpack storage. CurseForge only, see notes |
| [Call Your Horse](https://modrinth.com/mod/call-your-horse) | Blow a goat horn to whistle your horse over to you |
| [Clumps](https://modrinth.com/mod/ly-clumps) | Merges nearby experience orbs into one and picks them up instantly, which also cuts lag |
| [Day Counter](https://modrinth.com/mod/daycounter) | Shows the current day above the hotbar |
| [Spawn Animations](https://modrinth.com/mod/spawn-animations) | Hostile mobs dig out of the ground or poof into existence when they spawn |

Call Your Horse, Clumps, Day Counter and Spawn Animations are datapacks
packaged as mods, so players don't need them installed.

Also listed in compose: the five [Tensura libraries](#tensura-libraries).
Pulled in automatically: [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin) (VeinMiner)
and [Collective](https://modrinth.com/mod/collective) (Tree Harvester; a shared code library for
Serilum's mods that adds nothing on its own).

## Tensura libraries

Tensura's mod files require Architectury API, GeckoLib, SmartBrainLib,
TerraBlender and ManasCore, but its Modrinth pages don't list them, so
neither the server nor the Modrinth App would add them on their own. Without
them the game refuses to start. The player profile and the server both
include all five.

## Client mods

All of these are in the player profile. Client-only mods are not on the
server.

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
| [Better Inventory and Backpacks](https://www.curseforge.com/minecraft/mc-mods/better-inventory-and-backpacks) | **Yes** | Must match the server |
| [FTB Quests](https://www.curseforge.com/minecraft/mc-mods/ftb-quests-fabric) + [FTB Library](https://www.curseforge.com/minecraft/mc-mods/ftb-library-fabric) + [FTB Teams](https://www.curseforge.com/minecraft/mc-mods/ftb-teams-fabric) | **Yes** | Must match the server |
| [Certain Questing Additions](https://modrinth.com/mod/certain-questing-additions) | No | Animations and QoL for the FTB Quests book |
| [VeinMiner Hotkey](https://modrinth.com/mod/veinminer-client) | **Yes** | Hold a key to vein-mine; needs VeinMiner + Fabric Language Kotlin |
| [Tensura Voice](https://modrinth.com/mod/tensura-voice) | No | Voice of the World animations and sounds |
| [Sodium](https://modrinth.com/mod/sodium) | No | Rendering performance |
| [Iris](https://modrinth.com/mod/iris) | No | Shader loader, pinned to 1.8.14-beta.1 (see notes) |
| [Eclipse](https://modrinth.com/shader/eclipseshaders) | No | Shader pack, see notes below |
| [Complementary Reimagined](https://modrinth.com/shader/complementary-reimagined) | No | Shader pack: close to vanilla look, good performance |
| [Photon](https://modrinth.com/shader/photon-shader) | No | Shader pack: semi-realistic lighting and clouds; heavier |
| [Lithium](https://modrinth.com/mod/lithium) | No | Helps singleplayer; harmless on a server |
| [ImmediatelyFast](https://modrinth.com/mod/immediatelyfast) | No | HUD/text rendering performance |
| [Mod Menu](https://modrinth.com/mod/modmenu) | No | Mod list + config screens |
| [Falling Leaves](https://modrinth.com/mod/fallingleaves) | No | Needs Cloth Config |
| [Particle Rain](https://modrinth.com/mod/particle-rain) | No | Rain and snow particles |
| [Not Enough Animations](https://modrinth.com/mod/not-enough-animations) | No | Third-person animations |
| [AFK Cinematics](https://modrinth.com/mod/afk-cinematics) | No | Camera orbit when idle |
| [AppleSkin](https://modrinth.com/mod/appleskin) | No | Food and saturation HUD |
| [Inventory Profiles Next](https://modrinth.com/mod/inventory-profiles-next) | No | Take or put everything in a chest with one click or key, sorting, auto-refill. Needs libIPN + Fabric Language Kotlin |
| [Mouse Tweaks](https://modrinth.com/mod/mouse-tweaks) | No | Drag over slots to move or split stacks, scroll to move items |
| [Inventory HUD+](https://modrinth.com/mod/inventory-hud-plus-by-soulspeed) | No | Armor and tool durability on screen |
| [Fresh Animations](https://modrinth.com/resourcepack/fresh-animations) | No | Resource pack: animated vanilla mobs (blinking, breathing, smoother movement). Needs EMF + ETF (included). Turn it on under Options → Resource Packs |
| [Camera Overhaul](https://modrinth.com/mod/cameraoverhaul) | No | Camera tilts and sways with movement and turning |
| [Immersive Interfaces](https://modrinth.com/resourcepack/shrimps-immersive-interfaces) | No | Resource pack: redrawn GUI textures. Turn it on under Options → Resource Packs |
| [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap) | No | |
| [Xaero's World Map](https://modrinth.com/mod/xaeros-world-map) | No | |
| [Just Enough Items](https://modrinth.com/mod/jei) | No | Recipe viewer |
| [Dynamic FPS](https://modrinth.com/mod/dynamic-fps) | No | Lowers frame rate and volume when the game is in the background, idle or on battery |
| [Visuality](https://modrinth.com/mod/visuality) | No | Extra particles: mob hits, slime blobs, crystal sparkles, ambient effects; needs Cloth Config |
| [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights) | No | Torches and other light sources light up the area while held or dropped |

Also in the profile as dependencies: Cloth Config (Falling Leaves,
Visuality, Camera Overhaul), Placeholder API (Mod Menu),
Entity Model Features + Entity Texture Features (Fresh Animations),
Fabric Language Kotlin (VeinMiner) and the five Tensura libraries.

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
- **Spatial GUI:** removed 2026-10-20; bullet didn't like the 3D inventory
  screens.
- **Create Questing:** only made for 1.20.1 and older.
- **Global Server Config:** Forge only, and it solves a Forge problem
  (per-world `serverconfig` folders) that Fabric doesn't have.
- **Fresh & Smooth (modpack):** no 1.21.1 build. Its mods are listed under
  recommendations instead; adding all ~90 untested would be asking for a
  crash.
- **Voxy:** its first build is for 1.21.9. Nothing for 1.21.1.
- **Euphoria (modpack):** only made for 26.1.2, and a modpack can't go
  inside another modpack anyway. The shader add-on
  [Euphoria Patches](https://modrinth.com/mod/euphoria-patches) does support
  1.21.1 (see recommendations).

## Notes on the list

- **Iris and Sodium:** the newest Sodium for 1.21.1 (0.8.13) refuses to load
  with Iris older than 1.8.13, and the newest *release* of Iris for 1.21.1 is
  1.8.8. The profile pins **Iris 1.8.14-beta.1**, the pairing the TenSura
  modpack itself ships.
- **TerraBlender** has only ever published 1.21.1 builds marked beta, so it's
  pinned to 4.1.0.8 and the server allows beta versions.
- **Chunky:** it does nothing until it's told to. After the first start,
  run it once from the console, for example
  `docker exec minecraft rcon-cli chunky radius 2000` and then
  `docker exec minecraft rcon-cli chunky start`. It can be paused and resumed,
  and the size can be changed.
- **Tree Harvester + VeinMiner:** VeinMiner can also break whole veins of
  logs. If both would trigger on the same tree, turn logs off in VeinMiner.
- **Shader packs:** the profile has three, Eclipse, Complementary Reimagined
  and Photon. Pick one under Video Settings → Shader Packs; only one runs at a
  time. Eclipse is a single beta listed for 1.21.5–1.21.8 only and hasn't
  been tested on 1.21.1; the other two support 1.21.1. Shaders are the
  heaviest item on this list for a player's GPU.
- **JEI** is pinned to 19.51.0.418. Newer builds require mezz's config
  library, which only has beta releases.
- **Spawn Animations:** Modrinth lists Quilt's QSL as a requirement, but the
  Fabric jar doesn't need it, so `pack/mods.toml` skips it (`skip_deps`).
  The server log shows a few "Failed to load function
  spawnanimations:internal/entity/ehs/pehkui/..." errors on start; those are
  its hooks for the Pehkui mod, which isn't installed, and are harmless.
- **Cinematic AFK:** two similar mods exist, [AFK Cinematics](https://modrinth.com/mod/afk-cinematics)
  (listed above) and [Ji AFK Cinematic](https://modrinth.com/mod/ji-afk-cinematic).
  Use one, not both.
- **Better Inventory and Backpacks** is only on CurseForge. It isn't
  re-hosted here: the server downloads it through `MODS` in
  `docker-compose.yml`, and the profile points the Modrinth App at
  CurseForge's own download link. It changes how item stacks are saved, so
  removing it later can shrink or lose items in backpacks; the world was
  backed up before it was added.
- **FTB Quests** and its two libraries are CurseForge only (All Rights
  Reserved), handled the same way as Better Inventory. The quest book starts
  empty: an op opens it and turns on edit mode to write chapters and quests.
  They're saved in `data/config/ftbquests/`.
  The book comes with one chapter, **Tensura Milestones** (51 quests): the
  EP rank ladder from D to Special S Class, race evolution and awakening,
  abilities, taming and naming, the metal tiers up to Hihi'irokane, the
  Labyrinth and Hell, and the bosses (Tensura's and Not Enough Bosses').
  Each quest is one of Tensura's own advancements, so it completes by
  itself, progress from before the chapter existed included, and rewards
  XP levels. `pack/quests/tensura_milestones.py` wrote it; after the first
  load the in-game editor owns it, and the script won't overwrite it
  without `--force`.
- **ServerCore:** can lower view distance and slow far-away mobs when the
  server is busy. If Tensura mobs or MCA villagers act frozen at a distance,
  raise the activation ranges in `data/config/servercore/`.
- **Camera Overhaul** tilts the camera when strafing and turning. If that
  feels like it fights your movement: Mods → Camera Overhaul → set
  Strafing Roll Factor (and Mouselook Roll) to 0, or untick Enable.
- **Default keys:** Tensura takes Z, X, C (ability slots), V (dodge), B
  (Status Menu), N (naming), R (race ability) and Left Alt (next mode);
  Inventory HUD+ takes H and J. Nothing in the pack binds A, D or T.
- **Immersive Interfaces** is a beta resource pack (0.8.2) that covers
  1.21.1 through built-in overlays. It retextures vanilla screens, so Better
  Inventory's own inventory screen may not match it.
- **Tensura HUD:** Tensura hides the normal health and hunger bars and
  draws its own panel in the top-left (health, spiritual HP, magicules,
  aura). The profile ships `config/tensura/client/hud_config.toml` with the
  vanilla HUD back on and Tensura's top-left bars, food, armor and air turned
  off. Magicules and aura still show in the Status Menu. To get the panel
  back: Status Menu → Settings → HUD → Status Bars → Render Status Bars.
  The file only applies when the profile is imported; it doesn't touch an
  existing install.
- **Particle Rain:** none of the other mods add weather particles, so it
  doesn't overlap with anything.

## Recommendations (not added)

Server:

- [spark](https://modrinth.com/mod/spark): profiler for finding lag.
- [FerriteCore](https://modrinth.com/mod/ferrite-core): lower memory use;
  works on both server and client.
- [C2ME](https://modrinth.com/mod/c2me-fabric): faster chunk generation,
  which also makes Chunky faster. Only an alpha exists for 1.21.1.
- [Simple Voice Chat](https://modrinth.com/mod/simple-voice-chat): proximity
  voice chat. Needs an extra UDP port (24454) open.

Client:

- [Euphoria Patches](https://modrinth.com/mod/euphoria-patches): add-on for
  Complementary Reimagined with extra optional effects.
- [Entity Culling](https://modrinth.com/mod/entityculling): skips drawing
  mobs and block entities you can't see; pairs well with Sodium.
- [Sodium Extra](https://modrinth.com/mod/sodium-extra) and
  [Reese's Sodium Options](https://modrinth.com/mod/reeses-sodium-options):
  more video settings.
- [Jade](https://modrinth.com/mod/jade): shows what you're looking at.
- [Mouse Tweaks](https://modrinth.com/mod/mouse-tweaks): faster inventory
  handling (drag to move or split stacks, scroll to move items).
- [Inventory Profiles Next](https://modrinth.com/mod/inventory-profiles-next):
  sort buttons, locked slots, auto-refill of tools and blocks; heavier, adds
  buttons to every container screen.
- [Controlling](https://modrinth.com/mod/controlling): replacement for
  Keybind Atlas (needs Searchables).

## Running it

```sh
cp .env.example .env        # set RCON_PASSWORD
docker compose up -d        # start
docker compose logs -f      # watch it start up
docker compose down         # stop
```

## Changing the mod list

`pack/mods.toml` is the only list. Each mod is marked `both`, `server` or
`client`, and can pin a version. After editing it:

```sh
python3 pack/build.py 2026.10.20     # pack version, usually today's date
```

This resolves every mod and its dependencies against Modrinth, checks each
mod file's own `depends` (not just what its Modrinth page claims; Tensura is
why), rewrites the pinned `MODRINTH_PROJECTS` block in `docker-compose.yml`,
and builds `dist/bullets-server.mrpack`. Then commit, push, and publish the
profile:

```sh
gh release create pack-2026.10.20 dist/bullets-server.mrpack --title "Player profile 2026.10.20"
```

The download button always points at the newest release, so the asset name
must stay `bullets-server.mrpack`.

Then tell whoever is online, in the game chat:

```sh
python3 pack/announce.py profile "Added <mod> (<what it does>)"   # client mods: adds a clickable download link
python3 pack/announce.py server  "Added <mod>"                     # server-only mods
python3 pack/announce.py restart "Restarting in 30 seconds to add <mod>"
```

`data/` holds the world and runtime files and is not committed.
