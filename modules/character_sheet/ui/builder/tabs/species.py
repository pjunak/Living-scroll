from __future__ import annotations

from typing import Mapping
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel,
    QGroupBox, QScrollArea, QFrame
)

from modules.character_sheet.model import CharacterSheet
from modules.compendium.service import Compendium
from modules.compendium.modifiers.state import ModifierStateSnapshot
from modules.character_sheet.ui.builder.widgets.level_entry import LevelEntry

class SpeciesTab(QWidget):
    """
    Handles Species Selection and Species-specific dynamic traits (Lineages, Skills, etc).
    """
    dataChanged = Signal()

    def __init__(
        self,
        sheet: CharacterSheet,
        modifier_snapshot: ModifierStateSnapshot,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._sheet = sheet
        self._modifier_snapshot = modifier_snapshot
        self._selections = dict(sheet.feature_options)
        self._compendium = Compendium.load()
        
        self._species_combo: QComboBox | None = None
        self._species_entry: LevelEntry | None = None
        
        self._layout_ui()
        self._load_data()

    def _layout_ui(self):
        layout = QVBoxLayout(self)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        content = QWidget()
        self.form_layout = QVBoxLayout(content)
        self.form_layout.setSpacing(20)
        
        # 1. Species Selection Group
        self.form_layout.addWidget(self._build_species_section())
        
        # 2. Species Features Container
        self._features_container = QVBoxLayout()
        self.form_layout.addLayout(self._features_container)
        
        self.form_layout.addStretch()
        scroll.setWidget(content)
        layout.addWidget(scroll)

    def _build_species_section(self) -> QWidget:
        group = QGroupBox("Ancestry")
        layout = QHBoxLayout(group)
        
        layout.addWidget(QLabel("Species:"))
        
        self._species_combo = QComboBox()
        self._species_combo.setMinimumWidth(200)
        self._species_combo.addItem("(Select Species)", "")
        self._species_combo.currentIndexChanged.connect(self._on_species_changed)
        layout.addWidget(self._species_combo)
        layout.addStretch()
        
        return group

    def _load_data(self):
        species_records = [r for r in self._compendium.records("species") if isinstance(r, Mapping)]
        sorted_species = sorted(species_records, key=lambda x: str(x.get("name", "")))
        for r in sorted_species:
            self._species_combo.addItem(str(r.get("name")), r)
            
        current_species = self._sheet.identity.ancestry
        if current_species:
            idx = self._species_combo.findText(current_species)
            if idx >= 0:
                self._species_combo.setCurrentIndex(idx)
        
        self._refresh_features()

    def _on_species_changed(self):
        txt = self._species_combo.currentText()
        if txt == "(Select Species)":
            self._sheet.identity.ancestry = ""
        else:
            self._sheet.identity.ancestry = txt
            
        self._refresh_features()
        self.dataChanged.emit()

    def _refresh_features(self):
        if self._species_entry:
            self._species_entry.setParent(None)
            self._species_entry.deleteLater()
            self._species_entry = None
            
        sp_name = self._sheet.identity.ancestry
        if not sp_name:
            return
            
        sp_record = next((s for s in self._compendium.records("species") if isinstance(s, dict) and str(s.get("name", "")).lower() == str(sp_name).lower()), None)
        if not sp_record:
            return
            
        species_features = []
        for f in sp_record.get("features", []):
            species_features.append({"name": f.get("name", ""), "source": sp_name})
            
        # Helper for ability bonuses
        def process_ability_bonus(record, source_name, entry_widget):
            abo = record.get("ability_bonus_options")
            if abo and isinstance(abo, dict):
                choose = abo.get("choose", 0)
                amount = abo.get("amount", 1)
                allowed = abo.get("abilities", [])
                if choose > 0 and allowed:
                    from modules.character_sheet.ui.builder.utils.selection_helpers import get_available_attributes, SKILL_DROPDOWN_WIDTH
                    for i in range(choose):
                        opt_key = f"{source_name.lower().replace(' ', '_')}_ability_{i}"
                        current_attr = self._selections.get(opt_key, "")
                        options = get_available_attributes(
                            self._sheet, 
                            max_score=20, 
                            pending_selections=self._selections,
                            compendium=self._compendium
                        )
                        if "any" not in [a.lower() for a in allowed]:
                            options = [o for o in options if o.upper() in allowed]
                            
                        entry_widget.add_dynamic_option(
                            label=f"Ability Increase (+{amount})",
                            options=options,
                            current=current_attr,
                            key=opt_key,
                            width=SKILL_DROPDOWN_WIDTH,
                            group_id=source_name.lower().replace(' ', '_')
                        )
                        
        self._species_entry = LevelEntry(
            level=0,
            class_name="Species",
            features=species_features,
            parent=self
        )
        self._species_entry._header.setText(f"Species: {sp_name}")
        self._species_entry._remove_btn.hide()
        
        if sp_record: process_ability_bonus(sp_record, sp_name, self._species_entry)
        
        # Populate dynamic options explicitly (Lineages, Feats, Skills)
        for feat in species_features:
            feat_name = feat.get("name", "")
            feat_name_lower = feat_name.lower()
            group_key = f"origin_feat_{feat_name_lower.replace(' ', '_')}"
            
            if "versatile talent" in feat_name_lower or "skillful" in feat_name_lower:
                from modules.character_sheet.ui.builder.utils.selection_helpers import get_available_skill_proficiencies, SKILL_DROPDOWN_WIDTH
                available_skills = get_available_skill_proficiencies(self._sheet, self._selections)
                
                opt_key = f"{group_key}_skill_0"
                current_selection = self._selections.get(opt_key, "")
                
                self._species_entry.add_dynamic_option(
                    label=f"Choose Skill",
                    options=available_skills,
                    current=current_selection,
                    key=opt_key,
                    width=SKILL_DROPDOWN_WIDTH,
                    group_id=group_key
                )
                
            elif "bonus feat" in feat_name_lower or feat_name_lower == "versatile":
                from modules.character_sheet.ui.builder.widgets.asi_feat_widget import ASIFeatWidget
                asi_widget = ASIFeatWidget(
                    group_key=group_key,
                    level=0,
                    current_selection=self._selections.get(group_key, ""),
                    current_scores={name: self._sheet.get_ability(name).score for name in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]},
                    character_level=self._sheet.identity.level,
                    feat_only=True,
                    parent=self._species_entry
                )
                asi_widget.choiceChanged.connect(self._on_choice_changed)
                asi_widget.featSelected.connect(lambda f_name, e=self._species_entry, gk=group_key: self._on_feat_selected(f_name, e, gk))
                self._species_entry.add_choice_widget(asi_widget)
                
                curr = self._selections.get(group_key, "")
                if curr and not curr.startswith("ASI:"):
                    self._populate_feat_options(curr, self._species_entry, group_key)
                
            elif "draconic ancestry" in feat_name_lower:
                draconic_options = [
                    "Black (Acid)", "Blue (Lightning)", "Brass (Fire)", 
                    "Bronze (Lightning)", "Copper (Acid)", "Gold (Fire)", 
                    "Green (Poison)", "Red (Fire)", "Silver (Cold)", "White (Cold)"
                ]
                opt_key = f"{group_key}_ancestry"
                current_selection = self._selections.get(opt_key, "")
                self._species_entry.add_dynamic_option(
                    label="Choose Draconic Ancestry",
                    options=draconic_options,
                    current=current_selection,
                    key=opt_key,
                    width=200,
                    group_id=group_key
                )
                
            elif "fiendish legacy" in feat_name_lower:
                legacy_options = ["Abyssal", "Chthonic", "Infernal"]
                opt_key = f"{group_key}_legacy"
                current_selection = self._selections.get(opt_key, "")
                self._species_entry.add_dynamic_option(
                    label="Choose Fiendish Legacy",
                    options=legacy_options,
                    current=current_selection,
                    key=opt_key,
                    width=150,
                    group_id=group_key
                )
                
                # Tiefling Spellcasting Ability
                stat_options = ["INT", "WIS", "CHA"]
                stat_key = f"{group_key}_spellcasting_ability"
                current_stat = self._selections.get(stat_key, "")
                self._species_entry.add_dynamic_option(
                    label="Spellcasting Ability",
                    options=stat_options,
                    current=current_stat,
                    key=stat_key,
                    width=150,
                    group_id=group_key
                )
                
            elif "giant ancestry" in feat_name_lower:
                giant_options = [
                    "Cloud's Jaunt (Cloud Giant)",
                    "Fire's Burn (Fire Giant)",
                    "Frost's Chill (Frost Giant)",
                    "Hill's Tumble (Hill Giant)",
                    "Stone's Endurance (Stone Giant)",
                    "Storm's Thunder (Storm Giant)"
                ]
                opt_key = f"{group_key}_giant_ancestry"
                current_selection = self._selections.get(opt_key, "")
                self._species_entry.add_dynamic_option(
                    label="Choose Giant Ancestry",
                    options=giant_options,
                    current=current_selection,
                    key=opt_key,
                    width=250,
                    group_id=group_key
                )
                
            else:
                # Generic options parser block (for Data-Driven lineage options)
                feat_raw = next((f for f in sp_record.get("features", []) if f.get("name") == feat_name), {})
                options = feat_raw.get("options", [])
                if options:
                    opt_key = f"{group_key}_choice"
                    current_val = self._selections.get(opt_key, "")
                    
                    class OptionWrapper:
                        def __init__(self, l, v):
                            self.label = l
                            self.value = v
                            
                    wrapped_options = []
                    for o in options:
                        if isinstance(o, dict):
                            lbl = o.get("label") or o.get("name", "")
                            val = o.get("value") or o.get("name", "")
                            wrapped_options.append(OptionWrapper(lbl, val))
                        else:
                            wrapped_options.append(OptionWrapper(str(o), str(o)))
                            
                    if wrapped_options:
                        self._species_entry.add_dynamic_option(
                            label=f"Choose {feat_name}",
                            options=wrapped_options,
                            current=current_val,
                            key=opt_key,
                            width=200,
                            group_id=group_key
                        )
                        
                        # Add generic spellcasting ability drop if needed
                        if "gnomish lineage" in feat_name_lower:
                            stat_options = ["INT", "WIS", "CHA"]
                            stat_key = f"{group_key}_spellcasting_ability"
                            current_stat = self._selections.get(stat_key, "")
                            self._species_entry.add_dynamic_option(
                                label="Spellcasting Ability",
                                options=stat_options,
                                current=current_stat,
                                key=stat_key,
                                width=150,
                                group_id=group_key
                            )

        
        self._species_entry.choiceChanged.connect(self._on_choice_changed)
        self._features_container.addWidget(self._species_entry)

    def _on_feat_selected(self, feat_name: str, entry: LevelEntry, group_key: str):
        """Handle feat selection - show inline options for the feat."""
        entry.clear_dynamic_options(group_id=group_key)
        self._populate_feat_options(feat_name, entry, group_key)
        
    def _populate_feat_options(self, feat_name: str, entry: LevelEntry, group_key: str):
        """Look up feat and add dynamic options if it has any."""
        feat_record = next((feat for feat in self._compendium.records("feats") if isinstance(feat, dict) and feat.get("name", "").lower() == feat_name.lower()), None)
        
        if not feat_record:
            return
            
        from modules.character_sheet.ui.builder.utils.selection_helpers import (
            get_available_skill_proficiencies,
            get_available_skill_expertises,
            get_available_attributes,
            get_available_tool_proficiencies,
            SKILL_DROPDOWN_WIDTH
        )
        
        feat_key_base = f"{feat_name.lower().replace(' ', '_')}"
        
        # Attribute increase options
        attr_increase = feat_record.get("attribute_increase")
        if attr_increase and isinstance(attr_increase, list):
            attr_key = f"{feat_key_base}_attribute"
            available_attrs = get_available_attributes(
                self._sheet, 
                max_score=20, 
                pending_selections=self._selections,
                compendium=self._compendium
            )
            
            if "any" in [a.lower() for a in attr_increase]:
                options = available_attrs
            else:
                options = [a for a in attr_increase if a.upper() in available_attrs]
            
            increase_amount = 1 
            for i in range(increase_amount):
                opt_key = f"{attr_key}_{i}"
                current_selection = self._selections.get(opt_key, "")
                
                entry.add_dynamic_option(
                    label=f"Choose Attribute (+1)",
                    options=options,
                    current=current_selection,
                    key=opt_key,
                    width=SKILL_DROPDOWN_WIDTH,
                    group_id=group_key
                )
        
        # Skill proficiency fallback (e.g. Skilled)
        proficiency = feat_record.get("proficiency")
        if proficiency and isinstance(proficiency, dict):
            skills = proficiency.get("skills", [])
            if skills:
                skill_key = f"{feat_key_base}_skill_proficiency"
                current_skill = self._selections.get(skill_key, "")
                available_skills = get_available_skill_proficiencies(self._sheet, self._selections)
                
                if skills == ["any"] or "any" in skills:
                    options = available_skills
                else:
                    options = [opt for opt in available_skills if opt.value in skills]
                
                if options:
                    entry.add_dynamic_option(
                        label="Choose Skill Proficiency",
                        options=options,
                        current=current_skill,
                        key=skill_key,
                        width=SKILL_DROPDOWN_WIDTH,
                        group_id=group_key
                    )
                    
            tools = proficiency.get("tools", [])
            if tools:
                tool_key = f"{feat_key_base}_tool_proficiency"
                current_tool = self._selections.get(tool_key, "")
                available_tools = get_available_tool_proficiencies(self._sheet, self._selections)
                
                if tools == ["any"] or "any" in tools:
                    options = available_tools
                else:
                    options = [t for t in tools if t in available_tools]
                
                if options:
                    entry.add_dynamic_option(
                        label="Choose Tool Proficiency",
                        options=options,
                        current=current_tool,
                        key=tool_key,
                        width=SKILL_DROPDOWN_WIDTH,
                        group_id=group_key
                    )
                    
        # Feature Options specific to magic initiate etc.
        options = feat_record.get("options", [])
        if options:
            opt_key = f"{feat_key_base}_choice"
            current_val = self._selections.get(opt_key, "")
            
            class OptionWrapper:
                def __init__(self, l, v):
                    self.label = l
                    self.value = v
                    
            wrapped_options = []
            for o in options:
                if isinstance(o, dict):
                    wrapped_options.append(OptionWrapper(o.get("name", ""), o.get("name", "")))
                else:
                    wrapped_options.append(OptionWrapper(str(o), str(o)))
                    
            if wrapped_options:
                entry.add_dynamic_option(
                    label=f"Choose {feat_name} Option",
                    options=wrapped_options,
                    current=current_val,
                    key=opt_key,
                    width=200,
                    group_id=group_key
                )


    def _on_choice_changed(self, key: str, value: str):
        if value:
            self._selections[key] = value
            self._sheet.feature_options[key] = value
        else:
            self._selections.pop(key, None)
            self._sheet.feature_options.pop(key, None)
        self.dataChanged.emit()
