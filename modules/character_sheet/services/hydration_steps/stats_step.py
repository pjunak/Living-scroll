"""Step 2: Set base ability scores from CharacterData."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium


class BaseStatsStep:
    """Write raw point-buy / rolled scores onto the sheet's ability block."""

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        for ability, score in data.base_stats.items():
            if ability in sheet.abilities:
                sheet.abilities[ability].score = score
