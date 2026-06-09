"""Step 8: Dev-mode validation — produces warnings for illegal character states."""

from __future__ import annotations

import logging
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium

from modules.character_sheet.services.formula import evaluate_formula

log = logging.getLogger(__name__)


class ValidationWarning:
    """A single validation warning."""

    __slots__ = ("category", "message")

    def __init__(self, category: str, message: str) -> None:
        self.category = category
        self.message = message

    def __repr__(self) -> str:
        return f"[{self.category}] {self.message}"


class ValidationStep:
    """
    Run after the entire pipeline.  Checks game rules dynamically from
    compendium data and collects warnings.
    
    Validation produces **warnings, not errors**.  The character sheet
    is always generated regardless.  Warnings are only surfaced when
    ``developer_mode`` is enabled in global settings.
    """

    def __init__(self) -> None:
        self.warnings: List[ValidationWarning] = []

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        self.warnings.clear()

        self._check_multiclass_requirements(sheet, data, compendium)
        self._check_management_limits(sheet, data, compendium)
        self._check_duplicate_proficiencies(sheet)

        # Log collected warnings
        if self.warnings:
            for w in self.warnings:
                log.warning("Validation: %s", w)

    # ── Multiclass Ability Requirements ──────────────────────────────

    def _check_multiclass_requirements(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        if len(data.classes) <= 1:
            return

        for cls_data in data.classes:
            record = compendium.class_record(cls_data.class_name.lower())
            if not record:
                continue

            reqs = record.get("multiclass_requirements", {})
            for ability_key, min_score in reqs.items():
                # Handle "STR|DEX" (either or)
                abilities = [a.strip() for a in ability_key.split("|")]
                if not any(
                    sheet.abilities.get(a, None)
                    and sheet.abilities[a].score >= min_score
                    for a in abilities
                ):
                    self.warnings.append(
                        ValidationWarning(
                            "multiclass",
                            f"{cls_data.class_name} requires "
                            f"{ability_key} >= {min_score}, "
                            f"but current scores do not meet this.",
                        )
                    )

    # ── Management Limits ────────────────────────────────────────────

    def _check_management_limits(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        """Check that management states don't exceed their formula-based caps."""
        management_state = getattr(data, "management_state", {})

        for cls_data in data.classes:
            record = compendium.class_record(cls_data.class_name.lower())
            if not record:
                continue

            for mgmt_def in record.get("management", []):
                mgmt_id = f"{cls_data.class_name}:{mgmt_def['id']}"
                current = management_state.get(mgmt_id, [])
                max_formula = mgmt_def.get("max_formula")

                if max_formula and current:
                    try:
                        max_count = evaluate_formula(max_formula, sheet)
                    except Exception:
                        continue

                    if len(current) > max_count:
                        self.warnings.append(
                            ValidationWarning(
                                "management",
                                f"{mgmt_id}: has {len(current)} items "
                                f"but max is {max_count} (formula: {max_formula}).",
                            )
                        )

    # ── Duplicate Proficiencies ──────────────────────────────────────

    def _check_duplicate_proficiencies(self, sheet: "CharacterSheet") -> None:
        for attr in ("weapons", "armor", "tools"):
            items = getattr(sheet.proficiencies, attr, [])
            seen = set()
            for item in items:
                if item in seen:
                    self.warnings.append(
                        ValidationWarning(
                            "proficiency",
                            f"Duplicate {attr} proficiency: {item}",
                        )
                    )
                seen.add(item)
