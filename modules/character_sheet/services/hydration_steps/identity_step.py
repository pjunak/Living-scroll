"""Step 1: Map identity fields from CharacterData to CharacterSheet."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium


class IdentityStep:
    """Copy simple identity decisions onto the sheet."""

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        i_dest = sheet.identity
        i_src = data.identity

        i_dest.name = i_src.name
        i_dest.ancestry = i_src.ancestry

        if hasattr(i_dest, "ancestry_subtype"):
            i_dest.ancestry_subtype = i_src.ancestry_subtype

        i_dest.background = i_src.background
        i_dest.alignment = i_src.alignment
        i_dest.player = i_src.player_name
        i_dest.experience = i_src.xp
        i_dest.level_cap = i_src.level_cap
        i_dest.portrait_path = i_src.portrait_path
