"""Character Engine for evaluating final character states.

This module encapsulates the business rules for taking a plain (dumped) Pydantic CharacterSheet
and a Compendium instance to generate all the derived stats (Abilities, HP, AC, Initiative).
"""

from __future__ import annotations

import re
from typing import Any, Dict

from modules.character_sheet.model.model import CharacterSheet
from modules.dnd24_mechanics.armor_class import derive_armor_class


class CharacterEngine:
    """Calculates all dynamic and active values of a Character sheet."""

    def __init__(self, sheet: CharacterSheet, compendium: Any = None):
        self.sheet = sheet
        self.compendium = compendium

    def get_ability_breakdown(self, name: str) -> Dict[str, Any]:
        """Calculate ability score with breakdown of bonuses."""
        key = name.upper()
        
        try:
             block = self.sheet.get_ability(name)
             base = block.score
        except KeyError:
             base = 10
             
        asi_bonuses = []
        feat_bonuses = []
        species_bonuses = []
        
        # 1. Base Origin Bonuses (Species + Background)
        def add_origin_bonus(record: dict, source: str, display_name: str):
            # Fixed ability bonuses
            ab = record.get("ability_bonus")
            if ab and isinstance(ab, dict):
                if str(ab.get("ability", "")).upper() == key:
                    species_bonuses.append({
                        'source': display_name,
                        'value': int(ab.get("amount", 1))
                    })
            # Dynamic ability bonuses
            abo = record.get("ability_bonus_options")
            if abo and isinstance(abo, dict):
                choose = int(abo.get("choose", 0))
                amount = int(abo.get("amount", 1))
                if choose > 0:
                    for i in range(choose):
                        opt_key = f"{source.lower().replace(' ', '_')}_ability_{i}"
                        val = self.sheet.feature_options.get(opt_key, "")
                        if val.upper() == key:
                            species_bonuses.append({
                                'source': f"{display_name} Choice",
                                'value': amount
                            })

        if self.compendium:
            sp_name = self.sheet.identity.ancestry
            sp_record = next((s for s in self.compendium.records("species") if isinstance(s, dict) and str(s.get("name", "")).lower() == str(sp_name).lower()), None)
            if sp_record:
                add_origin_bonus(sp_record, sp_name, sp_name)

        # 1.5. Background Starting Feat & Attributes
        if self.compendium:
            bg_name = self.sheet.identity.background
            if bg_name:
                bg_record = next((b for b in self.compendium.records("backgrounds") if isinstance(b, dict) and str(b.get("name", "")).lower() == str(bg_name).lower()), None)
                if bg_record:
                    add_origin_bonus(bg_record, "background", "Background")
                    starting_feat = bg_record.get("starting_feat")
                    if starting_feat:
                        feat_record = self._find_feat(starting_feat)
                        if feat_record:
                            attr_increase = feat_record.get("attribute_increase", [])
                            if attr_increase and (key in [a.upper() for a in attr_increase] or "any" in [a.lower() for a in attr_increase]):
                                if len(attr_increase) == 1 and attr_increase[0].lower() != "any":
                                    feat_bonuses.append({'source': f'{starting_feat} (Background)', 'value': 1})
                                else:
                                    feat_key_base = f"{starting_feat.lower().replace(' ', '_')}_attribute"
                                    amount_added = 0
                                    for d_key, d_val in self.sheet.feature_options.items():
                                        if d_key.startswith(feat_key_base) and str(d_val).upper() == key:
                                            amount_added += 1
                                    if amount_added > 0:
                                        feat_bonuses.append({
                                            'source': f'{starting_feat} (Background)',
                                            'value': amount_added
                                        })

        # 2. Parse ASI/Feat selections from feature_options
        for opt_key, opt_value in self.sheet.feature_options.items():
            if not opt_value:
                continue

            if opt_value.startswith("ASI:"):
                # Parse ASI like "ASI:STR+2" or "ASI:STR+1,DEX+1"
                level_match = re.search(r'_asi_(\d+)$', opt_key)
                level = int(level_match.group(1)) if level_match else 0
                
                # Regex looks for XXX+1 or XXX+2 where XXX is the ability score code
                bonuses = re.findall(r'(\w{3})\+(\d+)', opt_value)
                for ability, amount in bonuses:
                    if ability.upper() == key:
                        asi_bonuses.append({
                            'source': f'ASI Level {level}' if level > 0 else 'ASI (Origin/Feat)',
                            'value': int(amount)
                        })
            else:
                # Might be a feat
                if self.compendium:
                    feat_record = self._find_feat(opt_value)
                    if feat_record:
                        attr_increase = feat_record.get("attribute_increase", [])
                        if attr_increase and (key in [a.upper() for a in attr_increase] or "any" in [a.lower() for a in attr_increase]):
                            # Look for dynamic attribute selection for this feat
                            if len(attr_increase) == 1 and attr_increase[0].lower() != "any":
                                feat_bonuses.append({'source': opt_value, 'value': 1})
                            else:
                                feat_key_base = f"{opt_value.lower().replace(' ', '_')}_attribute"
                                amount_added = 0
                                for d_key, d_val in self.sheet.feature_options.items():
                                    if d_key.startswith(feat_key_base) and str(d_val).upper() == key:
                                        amount_added += 1
                                if amount_added > 0:
                                    feat_bonuses.append({
                                        'source': opt_value,
                                        'value': amount_added
                                    })

        total = base + sum(b['value'] for b in species_bonuses) + sum(b['value'] for b in asi_bonuses) + sum(b['value'] for b in feat_bonuses)

        parts = [f"Base: {base}"]
        for b in species_bonuses:
            parts.append(f"{b['source']}: +{b['value']}")
        for b in asi_bonuses:
            parts.append(f"{b['source']}: +{b['value']}")
        for b in feat_bonuses:
            parts.append(f"{b['source']}: +{b['value']}")
        parts.append(f"Total: {total}")

        return {
            'base': base,
            'species_bonuses': species_bonuses,
            'asi_bonuses': asi_bonuses,
            'feat_bonuses': feat_bonuses,
            'total': total,
            'tooltip': '\n'.join(parts)
        }
        
    def _find_feat(self, name: str) -> Dict[str, Any] | None:
         """Look up a feat by name in the compendium."""
         if not self.compendium:
             return None
         try:
             for feat in self.compendium.records("feats"):
                 if isinstance(feat, dict) and feat.get("name", "").lower() == name.lower():
                     return feat
         except Exception:
             pass
         return None

    def get_ac_breakdown(self) -> Dict[str, Any]:
        """Calculate AC with breakdown using the central AC rules."""
        # For full decoupling we want `derive_armor_class` to do the heavy lifting
        # But for now we proxy current behavior or enhance it.
        
        # We need ability scores
        dex_breakdown = self.get_ability_breakdown("DEX")
        dex_score = dex_breakdown["total"]
        dex_mod = (dex_score - 10) // 2
        
        con_score = self.get_ability_breakdown("CON")["total"]
        con_mod = (con_score - 10) // 2
        
        wis_score = self.get_ability_breakdown("WIS")["total"]
        wis_mod = (wis_score - 10) // 2
        
        class_names = [cls.name for cls in self.sheet.identity.classes]
        
        mods = {"STR": (self.get_ability_breakdown("STR")["total"] - 10) // 2,
                "DEX": dex_mod,
                "CON": con_mod,
                "INT": (self.get_ability_breakdown("INT")["total"] - 10) // 2,
                "WIS": wis_mod,
                "CHA": (self.get_ability_breakdown("CHA")["total"] - 10) // 2}
                
        # To avoid circular calculations, we compute the derivation
        ac_breakdown = derive_armor_class(
            compendium=self.compendium,
            equipment=self.sheet.equipment,
            dex_modifier=dex_mod,
            con_modifier=con_mod,
            wis_modifier=wis_mod,
            class_names=class_names,
            species_name=self.sheet.identity.ancestry,
            ability_modifiers=mods
        )
        
        # Re-format to UI expected layout
        total_ac = ac_breakdown.total
        parts = [f"Base: {ac_breakdown.base}"]
        
        if ac_breakdown.dex_modifier_used:
             parts.append(f"DEX Modifier: {ac_breakdown.dex_modifier_used:+d}")
        if ac_breakdown.item_bonus:
             parts.append(f"Item Bonus: {ac_breakdown.item_bonus:+d}")
        if ac_breakdown.feature_bonus:
             parts.append(f"Feature Bonus: {ac_breakdown.feature_bonus:+d}")
        if ac_breakdown.formula:
             parts.append(f"Formula: {ac_breakdown.formula}")

        return {
            'base': ac_breakdown.base,
            'dex_mod': ac_breakdown.dex_modifier_used,
            'armor_bonus': ac_breakdown.item_bonus,
            'total': total_ac,
            'tooltip': '\n'.join(parts) + f"\nTotal: {total_ac}"
        }

    def _get_active_grants(self) -> List[tuple[str, Dict[str, Any]]]:
        """Aggregate Grants payloads from all active features and options."""
        if not self.compendium:
            return []
            
        grants_list = []
        choices = set(str(v).lower() for v in self.sheet.feature_options.values() if v)
        
        # 1. Species Data
        sp_name = self.sheet.identity.ancestry
        if sp_name:
            sp_record = next((s for s in self.compendium.records("species") if isinstance(s, dict) and str(s.get("name", "")).lower() == str(sp_name).lower()), None)
            if sp_record:
                if sp_record.get("grants"):
                    grants_list.append((sp_name, sp_record.get("grants", {})))
                for feat in sp_record.get("features", []):
                    if not isinstance(feat, dict):
                        continue
                    if feat.get("grants"):
                        grants_list.append((feat.get("name", "Species Feature"), feat.get("grants", {})))
                    for opt in feat.get("options", []):
                        if not isinstance(opt, dict):
                            continue
                        if str(opt.get("value", "")).lower() in choices:
                            if opt.get("grants"):
                                grants_list.append((opt.get("label", "Species Option"), opt.get("grants", {})))
                                
        # 2. Feats (from background or choices)
        feats_to_check = set()
        bg_name = self.sheet.identity.background
        if bg_name:
            bg_record = next((b for b in self.compendium.records("backgrounds") if isinstance(b, dict) and str(b.get("name", "")).lower() == str(bg_name).lower()), None)
            if bg_record and bg_record.get("starting_feat"):
                feats_to_check.add(str(bg_record.get("starting_feat")).lower())
                
        for val in self.sheet.feature_options.values():
            if val and not str(val).startswith("ASI:"):
                feats_to_check.add(str(val).lower())
                
        for feat_name in feats_to_check:
            feat_record = self._find_feat(feat_name)
            if feat_record and feat_record.get("grants"):
                grants_list.append((feat_record.get("name", "Feat"), feat_record.get("grants", {})))
                
        return grants_list

    def get_hp_breakdown(self) -> Dict[str, Any]:
        """Calculate HP with breakdown from class hit dice and CON modifier."""
        con_mod = (self.get_ability_breakdown("CON")["total"] - 10) // 2
        level = self.sheet.identity.level or 1
        con_contribution = con_mod * level
        
        base_hp = 0
        parts = []
        class_hps = []
        
        # Calculate from classes
        is_first_level = True
        for cls in self.sheet.identity.classes:
            if not self.compendium:
                continue
                
            class_record = self.compendium.class_record(cls.name)
            if not class_record:
                continue
                
            hit_die_str = class_record.get("hit_die", "d8")
            try:
                hit_die = int(hit_die_str.lower().replace("d", ""))
            except ValueError:
                hit_die = 8
                
            class_hp = 0
            for i in range(cls.level):
                if is_first_level:
                    class_hp += hit_die
                    is_first_level = False
                else:
                    class_hp += (hit_die // 2) + 1
                    
            base_hp += class_hp
            class_hps.append(f"{cls.name} ({cls.level} levels, d{hit_die}): {class_hp}")
            
        if base_hp == 0:
            # Fallback to manual value if parsing failed/no classes
            base_hp = self.sheet.combat.max_hp - con_contribution
            if base_hp < 1: base_hp = 1
            parts = [f"Hit Dice (Manual Base): {base_hp}"]
        else:
            parts.append("Base HP From Hit Dice:")
            for line in class_hps:
                parts.append(f"  {line}")
                
        # Add HP bonuses from active Features/Feats automatically
        feature_hp = 0
        feature_parts = []
        
        active_grants = self._get_active_grants()
        for source, grants in active_grants:
            hp_per_level = grants.get("hp_per_level", 0)
            if hp_per_level > 0:
                feature_hp += hp_per_level * level
                feature_parts.append(f"{source}: +{hp_per_level * level}")
        
        total = base_hp + con_contribution + feature_hp
        
        parts.append(f"CON Modifier × Level: {con_mod:+d} × {level} = {con_contribution:+d}")
        for line in feature_parts:
            parts.append(line)
            
        return {
            'base_hp': base_hp,
            'con_contribution': con_contribution,
            'total': total,
            'tooltip': '\n'.join(parts) + f"\nTotal: {total}"
        }

    def calculated_proficiency_bonus(self) -> int:
        """Calculate proficiency bonus from character level."""
        level = self.sheet.identity.level or 1
        return 2 + (level - 1) // 4

    def get_proficiency_breakdown(self) -> Dict[str, Any]:
        """Get proficiency bonus with calculation breakdown."""
        level = self.sheet.identity.level or 1
        bonus = self.calculated_proficiency_bonus()
        
        tooltip = f"Level {level}\n2 + (Level - 1) ÷ 4\n= 2 + ({level} - 1) ÷ 4\n= {bonus}"
        
        return {
            'level': level,
            'total': bonus,
            'tooltip': tooltip
        }

    def get_initiative_breakdown(self) -> Dict[str, Any]:
        """Calculate initiative with breakdown."""
        dex_mod = (self.get_ability_breakdown("DEX")["total"] - 10) // 2
        
        # Check for Alert feat
        other_bonus = 0
        feat_bonuses = []
        if self.compendium:
            has_alert = False
            bg_name = self.sheet.identity.background
            if bg_name:
                bg_record = next((b for b in self.compendium.records("backgrounds") if isinstance(b, dict) and str(b.get("name", "")).lower() == str(bg_name).lower()), None)
                if bg_record and bg_record.get("starting_feat", "").lower() == "alert":
                    has_alert = True
                    
            for val in self.sheet.feature_options.values():
                if val and str(val).lower() == "alert":
                    has_alert = True
                    break
                    
            if has_alert:
                prof_bonus = self.calculated_proficiency_bonus()
                other_bonus += prof_bonus
                feat_bonuses.append(f"Alert Feat: +{prof_bonus} (Proficiency)")
        
        total = dex_mod + other_bonus
        
        parts = [f"DEX Modifier: {dex_mod:+d}"]
        for line in feat_bonuses:
            parts.append(line)
            
        parts.append(f"Total: {total:+d}")
        
        return {
            'dex_mod': dex_mod,
            'other_bonus': other_bonus,
            'total': total,
            'tooltip': '\n'.join(parts)
        }

    def get_speed_breakdown(self) -> Dict[str, Any]:
        """Calculate movement speed."""
        base_speed = 30
        
        if self.compendium:
            sp_name = self.sheet.identity.ancestry
            sp_record = next((s for s in self.compendium.records("species") if isinstance(s, dict) and str(s.get("name", "")).lower() == str(sp_name).lower()), None)
            if sp_record:
                speed = sp_record.get("speed", 30)
                if isinstance(speed, int):
                    base_speed = speed

        bonus = 0
        bonus_parts = []
        # Dynamic Speed Modifiers from Grants
        active_grants = self._get_active_grants()
        for source, grants in active_grants:
            bonuses = grants.get("bonuses", {})
            speed_bonus = bonuses.get("speed", 0)
            if speed_bonus > 0:
                bonus += speed_bonus
                bonus_parts.append(f"{source}: +{speed_bonus} ft.")
                
        # Future expansions could add bonuses for Monk speed, etc. here
        
        total = base_speed + bonus
        
        parts = [f"Base Speed ({self.sheet.identity.ancestry or 'Unknown'}): {base_speed} ft."]
        
        for line in bonus_parts:
            parts.append(line)
            
        parts.append(f"Total: {total} ft.")
        
        return {
            'base': base_speed,
            'bonus': bonus,
            'total': total,
            'tooltip': '\n'.join(parts)
        }
