"""Step 3: Apply species (ancestry) traits from the Compendium."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium


class SpeciesStep:
    """
    Resolve the species record from the compendium and apply its grants
    (proficiencies, resistances, senses, speed, etc.) to the sheet.
    """

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        species_key = data.identity.ancestry
        if not species_key:
            return

        record = compendium.species_record(species_key)
        if not record:
            return

        grants = record.get("grants", {})

        # Proficiencies
        for skill in grants.get("skills", []):
            if sheet.proficiencies.skills.get(skill, 0) < 1:
                sheet.proficiencies.skills[skill] = 1

        for weapon in grants.get("weapons", []):
            if weapon not in sheet.proficiencies.weapons:
                sheet.proficiencies.weapons.append(weapon)

        for tool in grants.get("tools", []):
            if tool not in sheet.proficiencies.tools:
                sheet.proficiencies.tools.append(tool)

        for armor in grants.get("armor", []):
            if armor not in sheet.proficiencies.armor:
                sheet.proficiencies.armor.append(armor)

        # Resistances
        for resist in grants.get("resistances", []):
            if not hasattr(sheet, "resistances"):
                sheet.resistances = []
            if resist not in sheet.resistances:
                sheet.resistances.append(resist)

        # Speed
        speed = record.get("speed")
        if speed and hasattr(sheet, "speed"):
            sheet.speed = speed

        # Senses
        for sense_name, sense_range in grants.get("senses", {}).items():
            if not hasattr(sheet, "senses"):
                sheet.senses = {}
            sheet.senses[sense_name] = sense_range
