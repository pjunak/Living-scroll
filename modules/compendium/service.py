"""Rule compendium loader for the modular 2024 D&D SRD data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Set

import re

from modules.core.services.settings import get_settings
from modules.compendium.loader import CompendiumLoader

# Module-level cache for Compendium instances to avoid redundant disk I/O
_COMPENDIUM_CACHE: Dict[tuple, "Compendium"] = {}


def clear_compendium_cache() -> None:
    """Clear the cached compendium instances (e.g. after settings change)."""
    _COMPENDIUM_CACHE.clear()


@dataclass
class SpellGrant:
    spell: str
    always_prepared: bool = False


@dataclass
class GrantedSpellList:
    level: int
    spells: List[str]
    always_prepared: bool = False


class Compendium:
    """Lightweight accessor around the static JSON rule data."""

    def __init__(self, payload: Mapping[str, object]) -> None:
        self._payload = payload
        self._classes = _index_by_name(_record_iterable_from(payload.get("classes")))
        self._backgrounds = _index_by_name(_record_iterable_from(payload.get("backgrounds")))
        self._feats = _index_by_name(_record_iterable_from(payload.get("feats")))
        self._invocations = _index_by_name(_record_iterable_from(payload.get("invocations")))
        self.point_buy = payload.get("point_buy", {})
        self._by_id: Dict[str, object] = {}
        self._display_by_id: Dict[str, str] = {}
        self._rebuild_id_index()

    @classmethod
    def load(cls, ruleset: str | None = None, modules: Iterable[str] | None = None) -> "Compendium":
        settings = get_settings()

        # Use provided ruleset or fall back to settings
        target_ruleset = ruleset or settings.ruleset
        
        # Resolve the root data path using Settings logic
        # Accessing private member _get_compendium_root for now, or we can rely on settings to provide it if we update settings.py
        # But settings.py has `_get_compendium_root`. Let's assume we can access it or replicate logic simply via settings.
        # Actually, `Settings` has `_get_compendium_root`.
        # To be clean, we should expose it or use the one from settings.
        # Let's use `get_settings()._get_compendium_root().parent` which is `modules/compendium`.
        # `_get_compendium_root` returns `.../modules/compendium/data`.
        
        data_root = settings._get_compendium_root()
        
        # Active modules
        active_modules = set(modules) if modules is not None else settings.active_modules
        
        # Check cache before loading from disk
        modules_key = frozenset(active_modules) if active_modules else frozenset()
        cache_key = (str(target_ruleset), modules_key)
        
        if cache_key in _COMPENDIUM_CACHE:
            return _COMPENDIUM_CACHE[cache_key]
        
        # Load
        loader = CompendiumLoader(data_root)
        try:
            payload = loader.load(target_ruleset, active_modules)
        except Exception as e:
            # Fallback or re-raise?
            print(f"Error loading compendium: {e}")
            payload = {}

        instance = cls(payload)
        _COMPENDIUM_CACHE[cache_key] = instance
        return instance

    @property
    def payload(self) -> Mapping[str, object]:
        """Expose the raw payload so non-UI systems can reason over the data."""

        return self._payload

    def records(self, category: str) -> List[dict]:
        """Return a best-effort list of records for an arbitrary category (e.g. feats)."""

        records = self._payload.get(category, [])
        if isinstance(records, list):
            return list(records)
        return []

    def record_by_id(self, record_id: str) -> Optional[object]:
        """Resolve a stable id to its underlying record payload."""

        key = (record_id or "").strip()
        if not key:
            return None
        return self._by_id.get(key)

    def display_for_id(self, record_id: str) -> str:
        """Best-effort display label for an id (used for link rendering)."""

        key = (record_id or "").strip()
        if not key:
            return ""
        return self._display_by_id.get(key, key)

    # --- Internal ----------------------------------------------------
    def _rebuild_id_index(self) -> None:
        by_id: Dict[str, object] = {}
        display: Dict[str, str] = {}

        def _ingest_record(record: Mapping[str, object], *, fallback: str) -> None:
            record_id = record.get("id")
            record_id = record_id if isinstance(record_id, str) else ""
            record_id = record_id.strip() or fallback
            if not record_id:
                return
            by_id.setdefault(record_id, dict(record))
            name = record.get("name")
            title = record.get("title")
            label = name if isinstance(name, str) and name.strip() else (title if isinstance(title, str) and title.strip() else record_id)
            display.setdefault(record_id, str(label))

        # Index top-level list categories.
        for category in ("spells", "feats", "backgrounds", "species", "equipment", "invocations", "classes", "modifiers", "monsters"):
            items = self._payload.get(category)
            if isinstance(items, list):
                for entry in items:
                    if isinstance(entry, Mapping):
                        name = entry.get("name")
                        name = name if isinstance(name, str) else ""
                        fallback = f"{category}:{_key(name)}" if name else ""
                        _ingest_record(entry, fallback=fallback)

        # Index nested class components (subclasses/options/features) if present.
        classes = self._payload.get("classes")
        if isinstance(classes, list):
            for klass in classes:
                if not isinstance(klass, Mapping):
                    continue
                klass_name = klass.get("name")
                klass_name = klass_name if isinstance(klass_name, str) else ""
                klass_key = _key(klass_name)
                for subclass in (klass.get("subclasses") or []) if isinstance(klass.get("subclasses"), list) else []:
                    if not isinstance(subclass, Mapping):
                        continue
                    sub_name = subclass.get("name")
                    sub_name = sub_name if isinstance(sub_name, str) else ""
                    fallback = f"subclass:{klass_key}:{_key(sub_name)}" if klass_key and sub_name else ""
                    _ingest_record(subclass, fallback=fallback)

        # Index rules blocks as synthetic ids.
        rules = self._payload.get("rules")
        if isinstance(rules, Mapping):
            for key, value in rules.items():
                if not isinstance(key, str):
                    continue
                synthetic_id = f"rules:{key}"
                by_id.setdefault(synthetic_id, value)
                display.setdefault(synthetic_id, key)

        self._by_id = by_id
        self._display_by_id = display

    def class_record(self, name: str) -> Optional[dict]:
        return self._classes.get(_key(name))

    def subclass_record(self, class_name: str, subclass_name: str) -> Optional[dict]:
        klass = self.class_record(class_name)
        if not klass:
            return None
        return _index_by_name(klass.get("subclasses", [])).get(_key(subclass_name))

    def background_record(self, name: str) -> Optional[dict]:
        return self._backgrounds.get(_key(name))

    def feat_record(self, name: str) -> Optional[dict]:
        return self._feats.get(_key(name))

    def invocation_record(self, name: str) -> Optional[dict]:
        return self._invocations.get(_key(name))

    def invocations(self) -> List[dict]:
        """Return all invocation records defined in the compendium."""

        return list(self._invocations.values())

    def invocations_for_class(
        self,
        class_name: str,
        *,
        class_level: int,
        known_spells: Iterable[str] | None = None,
        known_features: Iterable[str] | None = None,
    ) -> List[dict]:
        """Filter invocations by class prerequisites and auxiliary requirements."""

        class_key = _key(class_name)
        spell_keys = _lowered_set(known_spells)
        feature_keys = _lowered_set(known_features)
        level = max(0, int(class_level))
        matches: List[dict] = []
        for record in self._invocations.values():
            if _invocation_matches(record, class_key, level, spell_keys, feature_keys):
                matches.append(record)
        return matches

    def spellcasting_ability_for(self, class_name: str, subclass_name: str | None = None) -> Optional[str]:
        subclass = self.subclass_record(class_name, subclass_name) if subclass_name else None
        if subclass:
            spellcasting = subclass.get("spellcasting")
            if isinstance(spellcasting, Mapping):
                ability = spellcasting.get("ability")
                if isinstance(ability, str):
                    return ability.upper()
        klass = self.class_record(class_name)
        if not klass:
            return None
        spellcasting = klass.get("spellcasting")
        if isinstance(spellcasting, Mapping):
            ability = spellcasting.get("ability")
            if isinstance(ability, str):
                return ability.upper()
        return None

    def subclasses_with_granted_spells(self, class_name: str) -> List[dict]:
        klass = self.class_record(class_name)
        if not klass:
            return []
        result: List[dict] = []
        for record in klass.get("subclasses", []) or []:
            if record.get("granted_spells"):
                result.append(record)
        return result

    def feats_with_spell_grants(self) -> List[dict]:
        return [feat for feat in self._feats.values() if feat.get("granted_spells")]


def _key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (name or "").strip().lower()).strip("_")


def _index_by_name(records: Iterable[Mapping[str, object]]) -> Dict[str, dict]:
    index: Dict[str, dict] = {}
    for record in records or []:
        name = record.get("name") if isinstance(record, Mapping) else None
        if not isinstance(name, str):
            continue
        index[_key(name)] = dict(record)
    return index


def _record_iterable_from(value: Any) -> Iterable[Mapping[str, object]]:
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    return []


def _lowered_set(values: Iterable[str] | None) -> Set[str]:
    return {_key(value) for value in (values or []) if value}


def _invocation_matches(
    record: Mapping[str, Any],
    class_key: str,
    class_level: int,
    known_spells: Set[str],
    known_features: Set[str],
) -> bool:
    prereqs = record.get("prerequisites") or []
    for requirement in prereqs:
        if not isinstance(requirement, Mapping):
            return False
        req_type = _key(str(requirement.get("type", "")))
        value = _key(str(requirement.get("value", "")))
        if req_type == "class":
            required_class = value
            if required_class and required_class != class_key:
                return False
            required_level = int(requirement.get("level", 1) or 1)
            if class_level < required_level:
                return False
        elif req_type == "spell":
            if value not in known_spells:
                return False
        elif req_type == "feature":
            if value not in known_features:
                return False
        else:
            return False
    return True

def get_module_metrics(module_path: Path) -> Dict[str, int]:
    """Analyze a module directory and return counts of its content types.
       Note: This acts on a raw directory path, so we use the Loader's logic lightly or just manual check.
       For now, we can delegate to Loader's internal methods or keep a simplified version.
    """
    if not module_path.exists():
        return {}
    
    # We can instantiate a temporary loader just for counting if we exposed access to listing.
    # But `get_module_metrics` was a standalone utility.
    # Let's simple check the directories.
    metrics = {}
    
    for category, name in [("classes", "Classes"), ("spells", "Spells"), ("feats", "Feats"), ("items", "Equipment")]:
       p = module_path / category
       if p.exists():
           count = len(list(p.glob(f"**/*.json")) + list(p.glob(f"**/*.md")))
           if count: metrics[name] = count
           
    return metrics


__all__ = ["Compendium", "clear_compendium_cache", "get_module_metrics"]
