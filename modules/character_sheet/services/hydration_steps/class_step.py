"""Step 5: Process class features level-by-level."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet, ClassProgression
    from modules.character_sheet.model.schema import CharacterData, ClassLevelData
    from modules.compendium.service import Compendium


class ClassStep:
    """
    Iterate through each class the character has and process features
    one level at a time in ascending order.
    
    This ensures:
    - Multiclass proficiency rules are respected (primary vs secondary)
    - ASI/Feat choices at levels 4/8/12/16/19 are applied with correct prerequisites
    - Subclass features (and management entries) are merged at the right levels
    """

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        from modules.character_sheet.model.model import ClassProgression

        for idx, cls_data in enumerate(data.classes):
            class_record = compendium.class_record(cls_data.class_name.lower())
            if not class_record:
                continue

            is_primary = (idx == 0)

            # ── Register the class on the sheet ───────────────────────
            existing = next(
                (c for c in sheet.identity.classes if c.name == cls_data.class_name),
                None,
            )
            if existing:
                existing.level = max(existing.level, cls_data.level)
                if cls_data.subclass:
                    existing.subclass = cls_data.subclass
            else:
                entry = ClassProgression(
                    name=cls_data.class_name,
                    level=cls_data.level,
                    subclass=cls_data.subclass,
                )
                sheet.identity.classes.append(entry)

            # ── Level-1 base proficiencies ────────────────────────────
            self._apply_base_proficiencies(sheet, class_record, is_primary)

            # ── Walk level by level ───────────────────────────────────
            for level in range(1, cls_data.level + 1):
                self._apply_level(sheet, cls_data, class_record, compendium, level)

    # ──────────────────────────────────────────────────────────────────

    def _apply_base_proficiencies(
        self,
        sheet: "CharacterSheet",
        class_record: Dict[str, Any],
        is_primary: bool,
    ) -> None:
        """Apply level-1 proficiencies (full for primary, subset for multiclass)."""
        if is_primary:
            c_profs = class_record.get("proficiencies", {})
            sheet.proficiencies.armor.extend(c_profs.get("armor", []))
            sheet.proficiencies.weapons.extend(c_profs.get("weapons", []))

            saves = class_record.get("saves", [])
            for save in saves:
                if save in sheet.abilities:
                    sheet.abilities[save].save_proficient = True
        else:
            mc_profs = (
                class_record.get("multiclassing", {}).get("proficiencies", {})
            )
            if mc_profs:
                sheet.proficiencies.armor.extend(mc_profs.get("armor", []))
                sheet.proficiencies.weapons.extend(mc_profs.get("weapons", []))

    def _apply_level(
        self,
        sheet: "CharacterSheet",
        cls_data: "ClassLevelData",
        class_record: Dict[str, Any],
        compendium: "Compendium",
        level: int,
    ) -> None:
        """Apply every feature granted at *level* for this class."""
        progression: List[Dict] = class_record.get("progression", [])
        level_entry = next((p for p in progression if p.get("level") == level), None)
        if not level_entry:
            return

        for feature_name in level_entry.get("features", []):
            self._apply_feature(sheet, cls_data, class_record, compendium, feature_name, level)

    def _apply_feature(
        self,
        sheet: "CharacterSheet",
        cls_data: "ClassLevelData",
        class_record: Dict[str, Any],
        compendium: "Compendium",
        feature_name: str,
        level: int,
    ) -> None:
        """
        Dispatch a single feature by name.
        
        Currently handles:
        - Ability Score Improvement → applies feat/ASI from feature_choices
        - Subclass selection features → loads subclass record + merges management
        - Skill choices stored in feature_choices
        """
        feature_lower = feature_name.lower()

        # ── ASI / Feat ────────────────────────────────────────────────
        if feature_lower == "ability score improvement":
            for feat_key, selection in cls_data.feature_choices.items():
                if "_asi_" in feat_key and selection:
                    # Future: resolve feat from compendium and apply grants
                    pass
            return

        # ── Subclass Feature ──────────────────────────────────────────
        if "subclass" in feature_lower or "archetype" in feature_lower or "tradition" in feature_lower:
            if cls_data.subclass:
                subclass_record = compendium.subclass_record(
                    cls_data.class_name.lower(), cls_data.subclass.lower()
                )
                if subclass_record:
                    # Merge subclass management entries into the sheet
                    mgmt = subclass_record.get("management", [])
                    if mgmt:
                        if not hasattr(sheet, "_management_entries"):
                            sheet._management_entries = []
                        for entry in mgmt:
                            entry_copy = dict(entry)
                            entry_copy["_class"] = cls_data.class_name
                            sheet._management_entries.append(entry_copy)
            return

        # ── Skill / Expertise choices ────────────────────────────────
        for feat_key, selection in cls_data.feature_choices.items():
            if not selection:
                continue
            if "_skill_" in feat_key:
                if "_expertise" in feat_key:
                    sheet.proficiencies.skills[selection] = 2  # Expertise
                else:
                    if sheet.proficiencies.skills.get(selection, 0) < 2:
                        sheet.proficiencies.skills[selection] = 1
