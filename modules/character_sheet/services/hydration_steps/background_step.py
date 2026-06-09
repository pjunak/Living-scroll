"""Step 4: Apply background — ability bonuses, proficiencies, Origin Feat."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium


class BackgroundStep:
    """
    Resolve the background from the compendium and apply its grants:
    - Ability score bonuses (+2/+1 or +1/+1/+1 in 2024 rules)
    - Skill proficiencies
    - Tool proficiencies
    - Origin Feat
    """

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        bg_id = data.identity.background
        if not bg_id:
            return

        background = compendium.background_record(bg_id)
        if not background:
            return

        # ── Ability Score Bonuses (2024 Rules) ────────────────────────
        # Backgrounds can grant +2/+1 or +1/+1/+1.  The user's specific
        # choices are stored in data.background_choices, e.g.:
        #   {"ability_bonus_1": "DEX+2", "ability_bonus_2": "CON+1"}
        for key, value in data.background_choices.items():
            if "ability_bonus" in key and value:
                # Parse "DEX+2" → ability="DEX", bonus=2
                parts = value.replace("+", " ").split()
                if len(parts) == 2:
                    ability, bonus_str = parts
                    try:
                        bonus = int(bonus_str)
                    except ValueError:
                        continue
                    if ability in sheet.abilities:
                        sheet.abilities[ability].score += bonus

        # ── Proficiencies ─────────────────────────────────────────────
        profs = background.get("proficiencies", {})

        for skill in profs.get("skills", []):
            if sheet.proficiencies.skills.get(skill, 0) < 1:
                sheet.proficiencies.skills[skill] = 1

        for tool in profs.get("tools", []):
            if tool not in sheet.proficiencies.tools:
                sheet.proficiencies.tools.append(tool)

        # ── Origin Feat (2024 Rules) ──────────────────────────────────
        origin_feat = background.get("origin_feat")
        if origin_feat:
            # Store the feat grant for later resolution (feats are complex)
            if not hasattr(sheet, "granted_feats"):
                sheet.granted_feats = []
            if origin_feat not in sheet.granted_feats:
                sheet.granted_feats.append(origin_feat)
