#!/usr/bin/env python3
"""Write the "Tensura Milestones" FTB Quests chapter into the server's config.

Every quest is an advancement task on one of Tensura's own advancements, so
quests complete by themselves, including for progress made before the
chapter existed (FTB Quests re-checks advancement tasks every few ticks).

Titles and descriptions are written inline. FTB Quests 2101 moves them into
quests/lang/en_us.snbt the first time it loads the file, so after that the
in-game editor owns the chapter. This script refuses to overwrite it unless
given --force.

Usage: python3 pack/quests/tensura_milestones.py [--force]
Stdlib only.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "data" / "config" / "ftbquests" / "quests" / "chapters" / "tensura_milestones.snbt"

# (key, advancement, icon, title, description, deps, x, y, xp levels, shape)
# Rows: EP rank ladder; race; abilities; taming; metals; places; bosses.
Q = [
    # --- the EP rank ladder ---
    ("reincarnated", "tensura:reincarnated", "tensura:race_reset_scroll", "Reincarnated",
     "Pick your race and start over in a new world.", [], 0, 0, 2, "gear"),
    ("empowerment", "tensura:empowerment", "tensura:slime_chunk", "Empowerment",
     "Kill a monster to gain Existence Points (EP) for the first time.", ["reincarnated"], 1.5, 0, 2, ""),
    ("d_rank", "tensura:d_rank", "tensura:low_magisteel_nugget", "D Class",
     "Reach 1,000 EP.", ["empowerment"], 3, 0, 3, ""),
    ("c_rank", "tensura:c_rank", "tensura:high_magisteel_nugget", "C Class",
     "Reach 3,000 EP.", ["d_rank"], 4.5, 0, 4, ""),
    ("b_rank", "tensura:b_rank", "tensura:mithril_nugget", "B Class",
     "Reach 6,000 EP.", ["c_rank"], 6, 0, 5, ""),
    ("a_rank", "tensura:a_rank", "tensura:orichalcum_nugget", "A Class",
     "Reach 10,000 EP. You are now a hazard.", ["b_rank"], 7.5, 0, 6, ""),
    ("sa_rank", "tensura:sa_rank", "tensura:pure_magisteel_nugget", "Special A Class",
     "Reach 100,000 EP. Calamity-level monster.", ["a_rank"], 9, 0, 8, ""),
    ("s_rank", "tensura:s_rank", "tensura:adamantite_nugget", "S Class",
     "Reach 400,000 EP. A walking disaster.", ["sa_rank"], 10.5, 0, 10, ""),
    ("ss_rank", "tensura:ss_rank", "tensura:hihiirokane_nugget", "Special S Class",
     "Reach 800,000 EP. A literal catastrophe.", ["s_rank"], 12, 0, 15, "hexagon"),

    # --- race ---
    ("grow_spurt", "tensura:grow_spurt", "tensura:royal_blood", "Growth Spurt",
     "Evolve your race for the first time.", ["d_rank"], 3, -1.5, 5, ""),
    ("mass_naming", "tensura:infamy_famous", "tensura:daemon_essence", "Infamy and Fame",
     "Earn a Mass Naming by finishing raids or killing human mobs without dying.", ["grow_spurt"], 4.5, -1.5, 8, ""),
    ("higher_form", "tensura:higher_form", "tensura:dragon_essence", "True Hero or Demon Lord",
     "Awaken as a Demon Lord or a Chosen Hero.", ["s_rank"], 10.5, -1.5, 20, "hexagon"),

    # --- abilities ---
    ("real_adventure", "tensura:real_adventure", "tensura:spatial_bag", "The Real Adventure",
     "Obtain your first ability.", ["reincarnated"], 0, 1.5, 2, ""),
    ("fast_learner", "tensura:fast_learner", "tensura:low_quality_magic_crystal", "Fast Learner",
     "Learn a skill, magic or battlewill.", ["real_adventure"], 1.5, 1.5, 3, ""),
    ("youre_a_wizard", "tensura:youre_a_wizard", "tensura:magic_tome", "You're a Wizard",
     "Use a Magic Tome.", ["fast_learner"], 3, 2.25, 3, ""),
    ("battlewill", "tensura:forbidden_manual", "tensura:battlewill_manual", "The Forbidden Manual",
     "Use a Battlewill Manual.", ["fast_learner"], 3, 0.75, 3, ""),
    ("master_skill", "tensura:master_skill", "tensura:medium_quality_magic_crystal", "Mastery",
     "Master any ability.", ["fast_learner"], 4.5, 1.5, 5, ""),
    ("master_unique", "tensura:master_unique_skill", "tensura:high_quality_magic_crystal", "Master of One Trade",
     "Master a Unique Skill.", ["master_skill"], 6, 1.5, 10, ""),

    # --- taming ---
    ("monster_tamer", "tensura:monster_tamer", "tensura:monster_leather_b", "Monster Tamer",
     "Tame any monster.", ["real_adventure"], 0, 3, 3, ""),
    ("tamed_a_slime", "tensura:tamed_a_slime", "tensura:slime_chunk", "I'm Not a Bad Slime!",
     "Tame a slime.", ["monster_tamer"], 1.5, 3.75, 2, ""),
    ("direwolf", "tensura:hear_me_direwolves", "tensura:monster_leather_a", "Hear Me, Direwolves!",
     "Tame a direwolf.", ["monster_tamer"], 1.5, 2.25, 3, ""),
    ("name_a_mob", "tensura:name_a_mob", "minecraft:name_tag", "Your Name Is...",
     "Name a mob. Named subordinates grow stronger.", ["monster_tamer"], 3, 3, 4, ""),
    ("star_wolf", "tensura:good_boy", "minecraft:bone", "Who's a Good Boy?",
     "Ride a Tempest Star Wolf.", ["direwolf", "name_a_mob"], 4.5, 2.6, 8, ""),
    ("ruler_of_monsters", "tensura:ruler_of_monster", "tensura:dark_jacket", "Ruler of Monsters",
     "Have a direwolf, goblin, lizardman, orc and slime as subordinates.", ["name_a_mob"], 4.5, 3.4, 10, ""),

    # --- metals ---
    ("silver", "tensura:acquire_silverware", "tensura:silver_ingot", "Silverware",
     "Smelt or find a Silver Ingot.", ["reincarnated"], 0, 4.5, 2, ""),
    ("magic_ore", "tensura:magic_ore", "tensura:magic_ore_shard", "Ore! But Magic?!",
     "Mine Magic Ore.", ["silver"], 1.5, 4.5, 3, ""),
    ("kiln", "tensura:better_smelter", "tensura:kiln", "The Kiln",
     "Craft a Kiln. Magisteel and the rare metals are mixed in it.", ["magic_ore"], 1.5, 5.25, 3, ""),
    ("low_magisteel", "tensura:low_magisteel", "tensura:low_magisteel_ingot", "Low Magisteel",
     "Mix iron with Magic Ore in a Kiln.", ["magic_ore"], 3, 4.5, 3, ""),
    ("high_magisteel", "tensura:high_magisteel", "tensura:high_magisteel_ingot", "High Magisteel",
     "Make a High Magisteel Ingot.", ["low_magisteel"], 4.5, 4.5, 4, ""),
    ("mithril", "tensura:mithril", "tensura:mithril_ingot", "Mithril",
     "Mix silver with Magic Ore in a Kiln.", ["high_magisteel"], 6, 4.5, 5, ""),
    ("orichalcum", "tensura:orichalcum", "tensura:orichalcum_ingot", "Orichalcum",
     "Mix gold with Magic Ore in a Kiln.", ["mithril"], 7.5, 4.5, 6, ""),
    ("pure_magisteel", "tensura:pure_magisteel", "tensura:pure_magisteel_ingot", "Pure Magisteel",
     "Acquire a Pure Magisteel Ingot.", ["orichalcum"], 9, 4.5, 8, ""),
    ("adamantite", "tensura:adamantite", "tensura:adamantite_ingot", "Adamantite",
     "Acquire an Adamantite item.", ["pure_magisteel"], 10.5, 4.5, 10, ""),
    ("hihiirokane", "tensura:hihiirokane", "tensura:hihiirokane_ingot", "Hihi'irokane",
     "Acquire a Hihi'irokane item: the ultimate metal.", ["adamantite"], 12, 4.5, 15, "hexagon"),

    # --- places ---
    ("trade", "tensura:delightful_trade", "tensura:bronze_coin", "A Deal-ightful Trade",
     "Complete a trade and earn coins.", ["reincarnated"], 0, 6, 2, ""),
    ("gold_coin", "tensura:my_precious", "tensura:gold_coin", "My Precious",
     "Obtain your first Gold Coin.", ["trade"], 1.5, 6, 4, ""),
    ("labyrinth", "tensura:labyrinth", "tensura:labyrinth_bricks", "Dungeon Encroachment",
     "Enter the Labyrinth.", ["reincarnated"], 3, 6, 4, ""),
    ("colossus_test", "tensura:just_a_test", "tensura:labyrinth_stone", "It's Just a Test!",
     "Fight the Elemental Colossus and \"die\".", ["labyrinth"], 4.5, 6, 4, ""),
    ("spirit", "tensura:elementalist", "tensura:labyrinth_praying_path", "Elementalist",
     "Form a contract with a Spirit.", ["colossus_test"], 6, 6.6, 6, ""),
    ("colossus", "tensura:spirit_protector", "tensura:pure_magisteel_block", "The Fairy Won't Like This",
     "Defeat the Elemental Colossus.", ["colossus_test"], 6, 5.4, 10, ""),
    ("hell", "tensura:hell", "tensura:daemon_essence", "Welcome to the Underworld",
     "Enter the Hell dimension.", ["real_adventure"], 7.5, 6, 6, ""),
    ("daemon", "tensura:hella_cool", "tensura:lesser_daemon_spawn_egg", "Hella Cool",
     "Have a daemon as a subordinate.", ["hell"], 9, 6, 8, ""),

    # --- bosses ---
    ("serpent", "tensura:hiss_tory", "tensura:serpent_scale", "Hiss-tory",
     "Slay a Tempest Serpent for its scales.", ["empowerment"], 0, 7.5, 4, ""),
    ("orc_disaster", "tensura:eat_or_be_eaten", "tensura:orc_disaster_head", "Eat or Be Eaten",
     "Defeat an Orc Disaster.", ["serpent"], 1.5, 7.5, 10, ""),
    ("ifrit", "tensura:conqueror_of_flames", "tensura:anti_magic_mask", "Conqueror of Flames",
     "Defeat a natural Ifrit.", ["serpent"], 3, 7.5, 10, ""),
    ("charybdis", "tensura:ruler_of_the_skies", "tensura:charybdis_core", "Ruler of the Skies",
     "Defeat a Charybdis.", ["serpent"], 4.5, 7.5, 12, ""),
    ("gazel", "tensura:hero_king", "tensura:ruhk", "The Hero King",
     "Defeat Gazel Dwargo, Hero King of the Dwarves.", ["serpent"], 6, 7.5, 12, ""),
    ("hinata", "tensura:great_saint_of_the_west", "tensura:moonlight", "The Great Saint of the West",
     "Defeat Hinata Sakaguchi.", ["serpent"], 7.5, 7.5, 15, ""),
    ("rimuru", "tensura_neb:monster_ruler", "tensura:chilled_slime", "The Monster Ruler",
     "Defeat Rimuru.", ["serpent"], 9, 7.5, 15, ""),
    ("carrion", "tensura_neb:lion_king", "tensura_neb:white_tiger_azure_dragon_halberd", "The Lion King",
     "Defeat Carrion.", ["rimuru"], 10.5, 7.5, 15, ""),
    ("luminous", "tensura_neb:queen_of_nightmares", "tensura_neb:night_rose", "The Queen of Nightmares",
     "Defeat Luminous Valentine.", ["carrion"], 12, 7.5, 20, "hexagon"),
]


def qid(*parts):
    """Stable 16-hex-digit FTB Quests ID. The top bit stays clear because
    FTB Quests parses IDs as a signed long and treats overflow as 'no ID'."""
    n = int.from_bytes(hashlib.sha256("/".join(("tensura_milestones",) + parts).encode()).digest()[:8], "big")
    return f"{(n & 0x7FFFFFFFFFFFFFFF) or 1:016X}"


def s(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def quest(key, adv, icon, title, desc, deps, x, y, xp, shape):
    lines = [
        "\t\t{",
        f"\t\t\tid: {s(qid(key))}",
        f"\t\t\ttitle: {s(title)}",
        f"\t\t\ticon: {s(icon)}",
        f"\t\t\tdescription: [{s(desc)}]",
        f"\t\t\tx: {x:.2f}d",
        f"\t\t\ty: {y:.2f}d",
    ]
    if shape:
        lines.append(f"\t\t\tshape: {s(shape)}")
    # FTB's own layout: one value per line, no commas.
    if deps:
        lines += ["\t\t\tdependencies: ["] + [f"\t\t\t\t{s(qid(d))}" for d in deps] + ["\t\t\t]"]
    lines += [
        "\t\t\ttasks: [{",
        f"\t\t\t\tid: {s(qid(key, 'task'))}",
        '\t\t\t\ttype: "advancement"',
        f"\t\t\t\tadvancement: {s(adv)}",
        '\t\t\t\tcriterion: ""',
        "\t\t\t}]",
        "\t\t\trewards: [{",
        f"\t\t\t\tid: {s(qid(key, 'reward'))}",
        '\t\t\t\ttype: "xp_levels"',
        f"\t\t\t\txp_levels: {xp}",
        "\t\t\t}]",
        "\t\t}",
    ]
    return "\n".join(lines)


def main():
    keys = {q[0] for q in Q}
    for q in Q:
        missing = [d for d in q[5] if d not in keys]
        if missing:
            sys.exit(f"{q[0]}: unknown dependency {missing}")
    if OUT.exists() and "--force" not in sys.argv:
        sys.exit(f"{OUT} already exists (it may hold in-game edits); pass --force to overwrite")
    body = "\n".join(quest(*q) for q in Q)
    text = f"""{{
\tid: {s(qid("chapter"))}
\tfilename: "tensura_milestones"
\ttitle: "Tensura Milestones"
\tsubtitle: ["From freshly reincarnated to True Hero or Demon Lord"]
\ticon: "tensura:race_reset_scroll"
\tgroup: ""
\torder_index: 0
\tdefault_quest_shape: ""
\tdefault_hide_dependency_lines: false
\tquests: [
{body}
\t]
\tquest_links: []
}}
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(Q)} quests")


if __name__ == "__main__":
    main()
