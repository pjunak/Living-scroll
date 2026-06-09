"""Step 6: Calculate derived stats — PB, HP, AC, spell slots, save DCs."""

from __future__ import annotations

import math
from typing import Any, Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium


# Standard multiclass spell-slot table (PHB 2024)
MULTICLASS_SLOT_TABLE: Dict[int, List[int]] = {
    1:  [2],
    2:  [3],
    3:  [4, 2],
    4:  [4, 3],
    5:  [4, 3, 2],
    6:  [4, 3, 3],
    7:  [4, 3, 3, 1],
    8:  [4, 3, 3, 2],
    9:  [4, 3, 3, 3, 1],
    10: [4, 3, 3, 3, 2],
    11: [4, 3, 3, 3, 2, 1],
    12: [4, 3, 3, 3, 2, 1],
    13: [4, 3, 3, 3, 2, 1, 1],
    14: [4, 3, 3, 3, 2, 1, 1],
    15: [4, 3, 3, 3, 2, 1, 1, 1],
    16: [4, 3, 3, 3, 2, 1, 1, 1],
    17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
    18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
    19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
    20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
}

PROFICIENCY_BY_LEVEL: Dict[int, int] = {
    1: 2, 2: 2, 3: 2, 4: 2,
    5: 3, 6: 3, 7: 3, 8: 3,
    9: 4, 10: 4, 11: 4, 12: 4,
    13: 5, 14: 5, 15: 5, 16: 5,
    17: 6, 18: 6, 19: 6, 20: 6,
}

# Hit die face values
HIT_DIE_MAP: Dict[str, int] = {
    "d6": 6, "d8": 8, "d10": 10, "d12": 12,
}

# Spellcasting progression weights for multiclass slot calculation
CASTER_WEIGHT: Dict[str, float] = {
    "full": 1.0,
    "half": 0.5,
    "third": 1 / 3,
    "pact": 0,       # Warlock uses its own pact slot table
    "none": 0,
    None: 0,
}


class DerivedStatsStep:
    """
    Calculate all derived values once the primary pipeline steps have run.
    
    - Proficiency Bonus (from total character level)
    - Hit Points (dual mode: average vs rolled)
    - Spell Slots (multiclass table merging)
    - Spell Save DC / Spell Attack Modifier
    """

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        total_level = self._total_level(data)

        self._apply_proficiency_bonus(sheet, total_level)
        self._apply_hp(sheet, data, compendium, total_level)
        self._apply_spell_slots(sheet, data, compendium)

    # ── Proficiency Bonus ───────────────────────────────────────────

    @staticmethod
    def _total_level(data: "CharacterData") -> int:
        return max(1, sum(c.level for c in data.classes))

    @staticmethod
    def _apply_proficiency_bonus(sheet: "CharacterSheet", total_level: int) -> None:
        pb = PROFICIENCY_BY_LEVEL.get(total_level, 2)
        if hasattr(sheet, "proficiency_bonus"):
            sheet.proficiency_bonus = pb

    # ── HP ──────────────────────────────────────────────────────────

    @staticmethod
    def _apply_hp(
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
        total_level: int,
    ) -> None:
        """
        Calculate HP based on hp_mode:
        - 'average': level 1 = max die + CON, levels 2+ = ceil(die/2)+1 + CON
        - 'rolled':  level 1 = max die + CON, levels 2+ = hp_rolls[level] + CON
        """
        con_mod = 0
        if hasattr(sheet, "abilities") and "CON" in sheet.abilities:
            con_mod = (sheet.abilities["CON"].score - 10) // 2

        hp_mode = getattr(data, "hp_mode", "average")
        hp_rolls = getattr(data, "hp_rolls", {})

        hp = 0
        cumulative_level = 0

        for cls_data in data.classes:
            record = compendium.class_record(cls_data.class_name.lower())
            if not record:
                continue

            die_str = record.get("hit_die", "d8")
            die_face = HIT_DIE_MAP.get(die_str, 8)

            for lvl_in_class in range(1, cls_data.level + 1):
                cumulative_level += 1

                if cumulative_level == 1:
                    # Level 1: always max die
                    hp += die_face + con_mod
                elif hp_mode == "rolled" and cumulative_level in hp_rolls:
                    hp += hp_rolls[cumulative_level] + con_mod
                else:
                    # Average rounded up
                    avg = math.ceil(die_face / 2) + 1
                    hp += avg + con_mod

        # ── Feat bonuses (e.g. Tough = +2 HP per level) ──────────────
        feat_hp_per_level = 0
        if hasattr(sheet, "granted_feats"):
            for feat_id in sheet.granted_feats:
                feat_rec = compendium.feat_record(feat_id)
                if feat_rec and feat_rec.get("grants", {}).get("hp_per_level"):
                    feat_hp_per_level += feat_rec["grants"]["hp_per_level"]

        hp += feat_hp_per_level * total_level

        if hasattr(sheet, "hit_points"):
            sheet.hit_points.maximum = hp
        elif hasattr(sheet, "hp"):
            sheet.hp = hp

    # ── Spell Slots ─────────────────────────────────────────────────

    @staticmethod
    def _apply_spell_slots(
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        """
        Merge multiclass caster levels via the standard multiclass slot table.
        Warlock pact slots are handled separately.
        """
        caster_levels = 0.0

        for cls_data in data.classes:
            record = compendium.class_record(cls_data.class_name.lower())
            if not record:
                continue

            casting = record.get("spellcasting") or {}
            progression = casting.get("progression", "none")
            weight = CASTER_WEIGHT.get(progression, 0)
            caster_levels += cls_data.level * weight

        effective_level = int(caster_levels)
        if effective_level <= 0:
            return

        slots = MULTICLASS_SLOT_TABLE.get(min(effective_level, 20), [])
        if hasattr(sheet, "spell_slots"):
            for i, count in enumerate(slots):
                if i < len(sheet.spell_slots):
                    sheet.spell_slots[i] = count
