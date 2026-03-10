"""Evaluation service for class/subclass feature rules."""

from __future__ import annotations

from typing import Dict, Iterable, List, Sequence

from modules.character_sheet.model import CharacterSheet, ClassProgression

from .definitions import CLASS_FEATURE_RULES
from .models import ClassFeatureRule, CharacterRuleSnapshot, FeatureOptionGroup


def _normalise(text: str | None) -> str:
    return (text or "").strip().lower()


def _class_level(
    classes: Sequence[ClassProgression],
    class_name: str,
    subclass_name: str | None = None,
) -> int:
    target_class = _normalise(class_name)
    target_subclass = _normalise(subclass_name)
    total = 0
    for entry in classes:
        if _normalise(entry.name) != target_class:
            continue
        if target_subclass and _normalise(entry.subclass) != target_subclass:
            continue
        total += max(0, int(entry.level))
    return total


class CharacterRulesService:
    """Determines which class/subclass features apply to a character."""

    def __init__(self, rules: Iterable[ClassFeatureRule] | None = None) -> None:
        self._rules: List[ClassFeatureRule] = list(rules or CLASS_FEATURE_RULES)

    @property
    def rules(self) -> List[ClassFeatureRule]:
        return list(self._rules)

    def evaluate(
        self,
        sheet: CharacterSheet,
        selections: Dict[str, str] | None = None,
    ) -> CharacterRuleSnapshot:
        classes = tuple(sheet.identity.classes or [])
        active: List[ClassFeatureRule] = []
        option_groups: List[FeatureOptionGroup] = []
        resolved_selections: Dict[str, str] = dict(selections or {})

        for rule in self._rules:
            class_level = _class_level(classes, rule.class_name, rule.subclass_name)
            if class_level < rule.min_level:
                continue
            active.append(rule)
            for group in rule.options:
                if class_level < max(1, group.min_level):
                    continue
                option_groups.append(group)
                resolved_selections[group.key] = self._resolve_selection(group, resolved_selections)

        return CharacterRuleSnapshot(active, option_groups, resolved_selections)

    @staticmethod
    def _resolve_selection(group: FeatureOptionGroup, selections: Dict[str, str]) -> str:
        if not group.choices:
            return selections.get(group.key, "")
        existing = selections.get(group.key)
        valid_values = {choice.value for choice in group.choices}
        if existing in valid_values:
            return existing
        if group.default and group.default in valid_values:
            return group.default
        return next(iter(valid_values), "")

    def validate_multiclass_requirements(self, sheet: CharacterSheet, new_class_name: str, compendium: Any) -> List[str]:
        """
        Check if the character meets prerequisites for multiclassing into `new_class_name`.
        Returns a list of failure reasons (strings). Empty list = Valid.
        Rules:
        1. Must meet reqs for ALL existing classes.
        2. Must meet reqs for the NEW class.
        """
        failures = []
        
        # 1. Check existing classes
        for entry in sheet.identity.classes:
            failures.extend(self._check_class_req(sheet, entry.name, compendium))
            
        # 2. Check new class (if not already present - technically same check)
        failures.extend(self._check_class_req(sheet, new_class_name, compendium))
        
        return sorted(list(set(failures)))

    def _check_class_req(self, sheet: CharacterSheet, class_name: str, compendium: Any) -> List[str]:
        # Look up class in compendium
        class_record = None
        for record in compendium.records("classes"):
             if record.get("name", "").lower() == class_name.lower() or record.get("id") == f"class:{class_name.lower()}":
                 class_record = record
                 break
                 
        if not class_record:
            return []
            
        reqs = class_record.get("multiclass_requirements")
        if not reqs:
            return []
            
        failures = []
        for ability, min_score in reqs.items():
            # Special case: '|' indicates OR (e.g. "STR|DEX")
            if '|' in ability:
                sub_abilities = ability.split('|')
                if not any(sheet.get_ability(a).score >= min_score for a in sub_abilities):
                    failures.append(f"{class_name} requires { ' or '.join(sub_abilities) } >= {min_score}")
            else:
                 if sheet.get_ability(ability).score < min_score:
                     failures.append(f"{class_name} requires {ability} >= {min_score}")
        return failures




__all__ = ["CharacterRulesService"]
