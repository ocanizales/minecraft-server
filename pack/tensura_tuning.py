#!/usr/bin/env python3
"""Apply the server's Tensura progression tuning to data/config/tensura/.

bullet found progression too slow (EP and ranks, skills, gear, early game),
so these roughly double the pace. Each line is (file, key, value, default).
Every key must appear exactly once in its file, so a renamed or duplicated
setting stops the script instead of editing the wrong line.

Usage: python3 pack/tensura_tuning.py [--defaults]   (restart the server after)
Stdlib only.
"""
import re
import sys
from pathlib import Path

CONFIG = Path(__file__).resolve().parent.parent / "data" / "config" / "tensura"

TUNING = [
    # EP: share of a slain enemy's EP absorbed as aura/magicule (percent).
    ("energy_config.toml", "baseAuraGain", "2.0", "1.0"),
    ("energy_config.toml", "maxAuraGain", "15.0", "10.0"),
    ("energy_config.toml", "baseMagiculeGain", "2.0", "1.0"),
    ("energy_config.toml", "maxMagiculeGain", "15.0", "10.0"),
    # Less EP lost when killing enemies weaker than you.
    ("energy_config.toml", "maxEPReductionPercentage", "75.0", "90.0"),
    # Learning a new ability (100 points to learn).
    ("ability/ability_config.toml", "learningPoint", "2", "1"),
    ("ability/ability_config.toml", "maxBonus", "6", "4"),
    ("ability/ability_config.toml", "learningCooldown", "5", "10"),
    ("ability/ability_config.toml", "failingPenaltyChance", "0.05", "0.1"),
    # Mastery. masteryPoint is stored per player when they first join.
    ("ability/ability_config.toml", "masteryPoint", "2", "1"),
    ("ability/ability_config.toml", "masteryHitMultiplier", "3", "2"),
    ("ability/ability_config.toml", "masteryKillMultiplier", "3", "2"),
    # Early game: two starting skills instead of one.
    ("reincarnation_config.toml", "skillNumber", "2", "1"),
    # Gear: a Fire Elemental Core charges a Kiln for longer and wears less.
    ("block_config.toml", "chargeDuration", "4800", "2400"),
    ("block_config.toml", "fireCoreCost", "50", "100"),
]


def main():
    defaults = "--defaults" in sys.argv
    for name, key, value, default in TUNING:
        path = CONFIG / name
        text = path.read_text()
        pattern = re.compile(rf"(?m)^(\s*{re.escape(key)}\s*=\s*)(\S+)\s*$")
        matches = pattern.findall(text)
        if len(matches) != 1:
            sys.exit(f"{name}: expected exactly one '{key}', found {len(matches)}")
        target = default if defaults else value
        old = matches[0][1]
        path.write_text(pattern.sub(rf"\g<1>{target}", text))
        print(f"{name:32} {key:26} {old:>8} -> {target}")


if __name__ == "__main__":
    main()
