"""
Rules Engine for 5th Edition (2024).
Responsible for rehydrating a full CharacterSheet from CharacterData (decisions).
This enforces the "Event Sourcing" pattern where the Sheet is a read-only result.
"""

from __future__ import annotations

from typing import List, Dict, Optional, Any

from modules.character_sheet.model.model import (
    CharacterSheet, CharacterIdentity, ProficiencySet, 
    ClassProgression, BackgroundSelection, AbilityBlock
)
from modules.character_sheet.model.schema import CharacterData, ClassLevelData
from modules.compendium.service import Compendium

class RulesEngine:
    def __init__(self, compendium: Compendium):
        self.compendium = compendium

    def hydrate(self, data: CharacterData) -> CharacterSheet:
        """
        Reconstruct a CharacterSheet from raw decisions (CharacterData).
        """
        sheet = CharacterSheet()
        
        # 1. Apply Identity (Name, XP, etc.)
        self._apply_identity(sheet, data)
        
        # 2. Apply Base Ability Scores
        self._apply_base_stats(sheet, data)
        
        # 3. Initialize Proficiency Set (Wipe existing)
        sheet.proficiencies = ProficiencySet()
        
        # 4. Apply Background (Proficiencies, Equipment) (TODO)
        self._apply_background(sheet, data)
        
        # 5. Apply Classes & Features (TODO)
        self._apply_classes(sheet, data)
        
        # 6. Apply Feats (TODO)
        pass
        
        # 7. Apply Equipment (TODO)
        # We might need to copy manual equipment list
        
        return sheet

    def _apply_identity(self, sheet: CharacterSheet, data: CharacterData):
        """Map simple identity fields."""
        i_dest = sheet.identity
        i_src = data.identity
        
        i_dest.name = i_src.name
        i_dest.ancestry = i_src.ancestry
        i_dest.ancestry_subtype = i_src.ancestry_subtype
        i_dest.background = i_src.background
        i_dest.alignment = i_src.alignment
        i_dest.player = i_src.player_name
        i_dest.experience = i_src.xp
        i_dest.level_cap = i_src.level_cap
        i_dest.portrait_path = i_src.portrait_path

    def _apply_base_stats(self, sheet: CharacterSheet, data: CharacterData):
        """Set base scores before bonuses."""
        for ability, score in data.base_stats.items():
            if ability in sheet.abilities:
                sheet.abilities[ability].score = score

    def _apply_background(self, sheet: CharacterSheet, data: CharacterData):
        """Apply background features."""
        bg_id = data.identity.background
        if not bg_id:
            return
            
        # Try to find background by ID or Name (compendium keys are often normalized)
        # Assuming compendium lookup works by ID
        background = self.compendium.background_record(bg_id)
        
        # Fallback: Try by name if ID lookup fails (common in early data mismatch)
        if not background:
            # This is a robust lookup if keys don't match exactly
            # But let's assume strict ID for new system
            return
            
        # Apply standard proficiencies
        profs = background.get("proficiencies", {})
        
        # Skills
        for skill in profs.get("skills", []):
            sheet.proficiencies.skills[skill] = 1 # 1 = Proficient
            
        # Tools
        for tool in profs.get("tools", []):
            if tool not in sheet.proficiencies.tools:
                sheet.proficiencies.tools.append(tool)
        
        # Equipment (Simple add)
        # In a real system, we'd parse the choices, but here we might just
        # rely on the 'equipment' list in CharacterData being the definitive source
        # for what the user *currently* has. 
        # Background equipment is usually "starting gear" which is added once.
        # Since this is rehydration, we DON'T add starting gear every time.
        # We assume data.equipment contains the inventory.
        pass

    def _apply_classes(self, sheet: CharacterSheet, data: CharacterData):
        """Iterate through class progression."""
        # 1. Copy progression list to identity.classes (Aggregating)
        for cls_data in data.classes:
            # Check if class already exists in sheet
            existing = next((c for c in sheet.identity.classes if c.name == cls_data.class_name), None)
            
            is_new_class = False
            if existing:
                # Update existing
                existing.level = max(existing.level, cls_data.level)
                if cls_data.subclass:
                    existing.subclass = cls_data.subclass
                entry = existing
            else:
                # Create new
                is_new_class = True
                entry = ClassProgression(
                    name=cls_data.class_name,
                    level=cls_data.level,
                    subclass=cls_data.subclass
                )
                sheet.identity.classes.append(entry)
            
            # 2. Apply Class Base Features (Only on first occurrence of class)
            if is_new_class:
                # 2024 Rules: Multiclassing gives partial proficiencies.
                # Primary = First class added to sheet
                is_primary = (sheet.identity.classes[0] == entry)
                
                class_record = self.compendium.class_record(cls_data.class_name.lower())
                if class_record:
                    if is_primary:
                        # Apply Primary Proficiencies
                        c_profs = class_record.get("proficiencies", {})
                        
                        # Armor & Weapons
                        sheet.proficiencies.armor.extend(c_profs.get("armor", []))
                        sheet.proficiencies.weapons.extend(c_profs.get("weapons", []))
                        
                        # Saving Throws
                        saves = class_record.get("saves", [])
                        for save in saves:
                            if save in sheet.abilities:
                                sheet.abilities[save].save_proficient = True
                    else:
                        # Multiclass Proficiencies (Subset)
                        # TODO: Implement MC subset rules (usually explicitly listed in class data)
                        # For now, minimal/none or specific list if available
                        mc_profs = class_record.get("multiclassing", {}).get("proficiencies", {})
                        if mc_profs:
                             sheet.proficiencies.armor.extend(mc_profs.get("armor", []))
                             sheet.proficiencies.weapons.extend(mc_profs.get("weapons", []))
                             # Skills usually 1 from list, handled via choices?
                             # MC often gives "Choose 1 skill".
                             # We need to expose that choice.
                             pass
            
            # 3. Apply User Choices (Feature Choices)
            # This is where we apply "rogue_skill_1": "Stealth"
            # We look at the 'options' map in ClassLevelData
            for feat_key, selection in cls_data.feature_choices.items():
                if "_skill_" in feat_key and selection:
                    # Generic skill selection
                    # Check if it's expertise or proficiency
                    if "_expertise" in feat_key:
                        # Ensure we don't downgrade if already expert?
                        # Just output result
                        sheet.proficiencies.skills[selection] = 2 # Expertise
                    else:
                        # Only set to 1 if not already expertise
                        if sheet.proficiencies.skills.get(selection, 0) < 2:
                            sheet.proficiencies.skills[selection] = 1
                            
                elif "_asi_" in feat_key and selection:
                    # Apply ASI handling (simple parse)
                    # "ASI:+2 DEX" or "feat:Actor"
                    pass # Implemented in specific ASI handler

