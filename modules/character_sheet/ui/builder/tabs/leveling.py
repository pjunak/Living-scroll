from __future__ import annotations

from typing import List, Dict, Any, Tuple
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame, QPushButton, QHBoxLayout, QDialog, QMessageBox
)
from PySide6.QtCore import QTimer

from modules.character_sheet.model import CharacterSheet, ClassProgression
from modules.compendium.modifiers.state import ModifierStateSnapshot
from modules.compendium.service import Compendium
from modules.dnd24_mechanics.character_rules.models import FeatureOptionGroup, FeatureOptionChoice
from modules.character_sheet.ui.builder.widgets.level_entry import LevelEntry
from modules.character_sheet.ui.builder.dialogs.class_selection import ClassSelectionDialog

# New Architecture Imports
from modules.character_sheet.model.schema import CharacterData, ClassLevelData
from modules.character_sheet.services.rules_engine import RulesEngine

class LevelingTab(QWidget):
    def __init__(
        self,
        sheet: CharacterSheet,
        modifier_snapshot: ModifierStateSnapshot,
        data: CharacterData = None,
        engine: RulesEngine = None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._sheet = sheet
        self._modifier_snapshot = modifier_snapshot
        
        # New Architecture: Data + Engine
        self._data = data 
        self._engine = engine
        
        # Fallback to internal if not provided (legacy support)
        if not self._engine:
            self._compendium = Compendium.load() 
        else:
            self._compendium = self._engine.compendium

        self._selections = dict(sheet.feature_options) 
        self._level_entries: List[LevelEntry] = []
        
        layout = QVBoxLayout(self)
        
        # Scrollable Area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        content = QWidget()
        self.content_layout = QVBoxLayout(content)
        self.content_layout.setSpacing(10)
        self.content_layout.addStretch() 
        self.scroll.setWidget(content)
        layout.addWidget(self.scroll)
        
        # Bottom Controls
        controls = QHBoxLayout()
        controls.addStretch()
        
        self.btn_add_level = QPushButton("Add Class Level...")
        self.btn_add_level.clicked.connect(self._on_add_level_clicked)
        self.btn_add_level.setStyleSheet("font-weight: bold; background-color: #4ec9b0; color: black;")
        controls.addWidget(self.btn_add_level)
        layout.addLayout(controls)
        
        self.refresh_from_sheet()

    def _find_data_index(self, class_name: str, class_level: int) -> int:
        """Find the index in data.classes for the Nth level of a class."""
        if not self._data:
            return -1
        count = 0
        for i, entry in enumerate(self._data.classes):
            if entry.class_name == class_name:
                count += 1
                if count == class_level:
                    return i
        return -1
        
    def _on_feature_changed(self, index: int, key: str, value: str):
        """Handle dynamic option updates from LevelEntry."""
        if not self._data or index < 0 or index >= len(self._data.classes):
            return
        
        # Update Decision
        if value:
            self._data.classes[index].feature_choices[key] = value
        else:
            if key in self._data.classes[index].feature_choices:
                del self._data.classes[index].feature_choices[key]
        
        # Rehydrate
        self._sheet = self._engine.hydrate(self._data)
        
        # Refresh UI
        self.refresh_from_sheet()

    def _on_add_level_clicked(self):
        """Add a new class level."""
        dialog = ClassSelectionDialog(self._sheet, self, self._compendium)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
            
        selected_class = dialog.get_selected_class()
        if not selected_class:
            return

        # Update Decisions
        if self._data:
            new_level = ClassLevelData(
                class_name=selected_class,
                level=self._get_next_class_level(selected_class)
            )
            self._data.classes.append(new_level)
            
            # Rehydrate
            self._sheet = self._engine.hydrate(self._data)
            self.refresh_from_sheet()
        else:
            # Legacy Path not supported for adding levels in this refactor
            QMessageBox.warning(self, "Legacy Mode", "Cannot add levels to legacy character sheet. Please migrate.")

    def _on_remove_level_clicked(self, ordinal_level: int):
        """Remove a specific level. Note: 'level' arg from widget represents ordinal level of that class."""
        # This signal comes from the LevelEntry widget.
        # But wait, LevelEntry emits 'self.level', which is "Rogue 3" -> 3.
        # But we don't know WHICH class triggered it if we don't check sender or capture context.
        # I connected it with: entry.removeClicked.connect(lambda l, e=entry: self._on_remove_entry_clicked(e))
        pass

    def _on_remove_entry_clicked(self, entry: LevelEntry):
         # My _find_data_index helper solves this!
         data_idx = self._find_data_index(entry.class_name, entry.level)
         if data_idx != -1 and self._data:
             self._data.classes.pop(data_idx)
             self._sheet = self._engine.hydrate(self._data)
             self.refresh_from_sheet()

    def _get_next_class_level(self, class_name: str) -> int:
        if self._data:
             count = sum(1 for c in self._data.classes if c.class_name == class_name)
             return count + 1
        return 1

    def refresh_from_sheet(self):
        """Rebuild the timeline based on current data/sheet state."""
        v_scroll_val = self.scroll.verticalScrollBar().value()
        
        # Clear existing
        for entry in self._level_entries:
            entry.setParent(None)
            entry.deleteLater()
        self._level_entries.clear()
        
        # Remove widgets from layout
        while self.content_layout.count() > 1:
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
                
        # Iterate classes (Consolidated View from Hydrated Sheet)
        for class_prog in self._sheet.identity.classes:
            class_name = class_prog.name
            target_level = class_prog.level
            
            # Fetch compendium data
            class_record = self._compendium.class_record(class_name)
            
            # Iterate levels 1 to target_level
            for lvl in range(1, target_level + 1):
                # Find corresponding Data Source Index
                data_idx = self._find_data_index(class_name, lvl)
                
                # Get current choices for this level
                current_choices = {}
                if self._data and data_idx != -1:
                    current_choices = self._data.classes[data_idx].feature_choices
                else:
                    current_choices = self._selections # Fallback
                
                # Features from Compendium
                features_data = self._get_features_for_level(class_record, lvl, class_prog.subclass)
                
                entry = LevelEntry(lvl, class_name, features_data, parent=self)
                entry.choiceChanged.connect(lambda k, v, idx=data_idx: self._on_feature_changed(idx, k, v))
                entry.removeClicked.connect(lambda l, e=entry: self._on_remove_entry_clicked(e))
                
                # Dynamic Options: Skill Proficiency (Level 1 Primary Only)
                is_primary_level_1 = (data_idx == 0)
                if is_primary_level_1 and class_record:
                    profs = class_record.get("proficiencies", {})
                    skills_choose = profs.get("skills_choose", 0)
                    skill_list = profs.get("skill_list", [])
                    
                    if skills_choose > 0 and skill_list:
                        from modules.character_sheet.ui.builder.utils.selection_helpers import get_available_skill_proficiencies, SKILL_DROPDOWN_WIDTH
                        
                        # Calculate available based on sheet state (hydrated)
                        # We pass empty pending because sheet.proficiencies already HAS logic
                        available_all = get_available_skill_proficiencies(self._sheet, {})
                        
                        # Special handling: Since rehydration applies choices, the choice IS 'taken' in the sheet.
                        # The UI needs to show it as selected but allowing swap to others.
                        # get_available_skill_proficiencies filters out distinct taken skills.
                        # We should trust it returns what's legal to TAKE.
                        # But if I selected "Stealth" and it is hydrated, "Stealth" is in sheet.proficiencies.
                        # get_available_skill_proficiencies will NOT return "Stealth" because it's taken.
                        # This breaks the dropdown (current value "Stealth" is not in options).
                        # FIX: We must pass 'current choice' as allowed, OR manually inject it back into list if valid.
                        
                        available_profs = [opt.value for opt in available_all] # Just names
                        
                        for i in range(skills_choose):
                            key = f"{class_name.lower()}_skill_{i+1}"
                            current_val = current_choices.get(key, "")
                            
                            # Build options list specifically for this dropdown
                            # Include ALL available + current choice
                            dropdown_options = list(available_all)
                            
                            # If current selection exists and isn't in available (because it's taken), add it back
                            if current_val and current_val not in available_profs:
                                # We need to create a FeatureOptionChoice for it
                                # But we should check if it's in the class list first
                                if current_val in skill_list:
                                    dropdown_options.append(FeatureOptionChoice(label=current_val, value=current_val, enabled=True))
                            
                            # Normalize skill list for case-insensitive matching
                            skill_list_lower = {s.lower() for s in skill_list}

                            # Filter to class list (Case Insensitive)
                            final_choices = [
                                opt for opt in dropdown_options 
                                if opt.value.lower() in skill_list_lower
                            ]
                            
                            # Sort?
                            final_choices.sort(key=lambda x: x.label)

                            entry.add_dynamic_option(
                                label="Choose Skill Proficiency",
                                options=final_choices,
                                current=current_val,
                                key=key,
                                width=SKILL_DROPDOWN_WIDTH
                            )

                self._populate_feat_options(entry, features_data, current_choices)

                self.content_layout.insertWidget(self.content_layout.count() - 1, entry)
                self._level_entries.append(entry)

        # Restore scroll
        QTimer.singleShot(0, lambda: self.scroll.verticalScrollBar().setValue(v_scroll_val))

    def _get_features_for_level(self, class_record: Dict[str, Any] | None, level: int, subclass_name: str | None = None) -> List[Dict[str, Any]]:
        """Get features from class progression and subclass (if applicable) for a given level."""
        if not class_record:
            return []
        features = []
        
        # 1. Class Progression Features
        progression = class_record.get("progression", [])
        if isinstance(progression, list):
            for entry in progression:
                if not isinstance(entry, dict):
                    continue
                if entry.get("level") == level:
                    for feat_name in entry.get("features", []):
                        features.append({"name": feat_name, "source": class_record.get("name", "Class")})
        
        # 2. Subclass Features (if subclass is selected)
        if subclass_name:
            subclasses = class_record.get("subclasses", [])
            for sub in subclasses:
                if not isinstance(sub, dict):
                    continue
                if sub.get("name", "").lower() == subclass_name.lower():
                    sub_progression = sub.get("progression", [])
                    if isinstance(sub_progression, list):
                        for entry in sub_progression:
                            if not isinstance(entry, dict):
                                continue
                            if entry.get("level") == level:
                                for feat_name in entry.get("features", []):
                                    features.append({"name": feat_name, "source": sub.get("name", "Subclass")})
                    break
        
        return features

    def _populate_feat_options(self, entry: LevelEntry, features: List[dict], current_choices: Dict[str, str]):
        """Helper to add options based on feats in the level."""
        for feat in features:
             # Logic to detect feats
             feat_name = feat.get("name")
             self._add_feat_options_to_entry(entry, feat_name, current_choices)

    def _add_feat_options_to_entry(self, entry: LevelEntry, feat_name: str, current_choices: Dict[str, str]):
        """Look up feat and add dynamic options."""
        # Find feat in compendium
        feat_record = None
        for feat in self._compendium.records("feats"):
            if isinstance(feat, dict) and feat.get("name", "").lower() == feat_name.lower():
                feat_record = feat
                break
        
        if not feat_record:
            return
        
        from modules.character_sheet.ui.builder.utils.selection_helpers import (
            get_available_skill_proficiencies,
            get_available_skill_expertises,
            get_available_attributes,
            SKILL_DROPDOWN_WIDTH
        )
        
        feat_key_base = f"{feat_name.lower().replace(' ', '_')}"
        
        # Attribute increase options
        attr_increase = feat_record.get("attribute_increase")
        if attr_increase and isinstance(attr_increase, list):
            attr_key = f"{feat_key_base}_attribute"
            current_attr = current_choices.get(attr_key, "")
            
            available_attrs = get_available_attributes(
                self._sheet, 
                max_score=20, 
                pending_selections={}, 
                compendium=self._compendium
            )
            
            if "any" in [a.lower() for a in attr_increase]:
                options = available_attrs
            else:
                options = [a for a in attr_increase if a.upper() in available_attrs]
            
            if options:
                entry.add_dynamic_option(
                    label="Choose Attribute (+1)",
                    options=options,
                    current=current_attr,
                    key=attr_key,
                    width=SKILL_DROPDOWN_WIDTH
                )
        
        # Skill proficiency options
        proficiency = feat_record.get("proficiency")
        if proficiency and isinstance(proficiency, dict):
            skills = proficiency.get("skills", [])
            if skills:
                skill_key = f"{feat_key_base}_skill_proficiency"
                current_skill = current_choices.get(skill_key, "")
                
                # Logic to allow current selection
                available_skills = get_available_skill_proficiencies(self._sheet, {})
                available_profs = [opt.value for opt in available_skills]
                
                dropdown_options = list(available_skills)
                if current_skill and current_skill not in available_profs:
                     if skills == ["any"] or "any" in skills or current_skill in skills:
                        dropdown_options.append(FeatureOptionChoice(label=current_skill, value=current_skill, enabled=True))
                
                if skills == ["any"] or "any" in skills:
                    options = dropdown_options
                else:
                    options = [opt for opt in dropdown_options if opt.value in skills]
                
                if options:
                    entry.add_dynamic_option(
                        label="Choose Skill Proficiency",
                        options=options,
                        current=current_skill,
                        key=skill_key,
                        width=SKILL_DROPDOWN_WIDTH
                    )
        
        # Expertise options
        expertise = feat_record.get("expertise")
        if expertise and isinstance(expertise, dict):
            expert_skills = expertise.get("skills", [])
            if expert_skills:
                expertise_key = f"{feat_key_base}_skill_expertise"
                current_expertise = current_choices.get(expertise_key, "")
                
                available_expertise = get_available_skill_expertises(
                    self._sheet, 
                    pending_selections={}
                )
                 # Logic to allow current selection
                available_vals = [opt.value for opt in available_expertise]
                dropdown_options = list(available_expertise)
                
                if current_expertise and current_expertise not in available_vals:
                     if expert_skills == ["any"] or "any" in expert_skills or current_expertise in expert_skills:
                        dropdown_options.append(FeatureOptionChoice(label=current_expertise, value=current_expertise, enabled=True))

                if expert_skills == ["any"] or "any" in expert_skills:
                    options = dropdown_options
                else:
                    options = [o for o in dropdown_options if o.value in expert_skills]
                    
                if options:
                    entry.add_dynamic_option(
                        label="Choose Expertise", 
                        options=options,
                        current=current_expertise,
                        key=expertise_key,
                        width=SKILL_DROPDOWN_WIDTH
                    )
