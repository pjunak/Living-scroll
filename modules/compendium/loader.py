"""Filesystem loader for compendium data."""

from __future__ import annotations

import json
import yaml
from pathlib import Path
from typing import Any, Dict, List, Set, Iterable, Optional

class CompendiumLoader:
    """Handles loading and merging of compendium data from the filesystem."""
    
    def __init__(self, root_path: Path):
        self.root_path = root_path

    def load(self, ruleset: str, active_modules: Optional[Set[str]] = None) -> Dict[str, Any]:
        """Load and merge data for a specific ruleset and active modules."""
        target_path = self.root_path / ruleset
        if not target_path.exists():
            raise FileNotFoundError(f"Ruleset not found at {target_path}")

        combined_payload: Dict[str, Any] = {}
        
        # Determine sorting to ensure deterministic order
        # Simple alphabetical sort of module directories
        for module_dir in sorted(target_path.iterdir()):
            if not module_dir.is_dir() or module_dir.name.startswith("_"):
                continue
            
            if active_modules is not None and module_dir.name not in active_modules:
                continue

            module_payload = self._load_module(module_dir)
            combined_payload = self._merge_payloads(combined_payload, module_payload)
            
        return combined_payload

    def _load_module(self, module_path: Path) -> Dict[str, Any]:
        """Load all data from a single module directory."""
        payload: Dict[str, Any] = {}
        
        # Load metadata
        metadata_file = module_path / "metadata.json"
        if metadata_file.exists():
            payload["metadata"] = self._read_json(metadata_file)
            
        # Define the directory-to-category mapping
        categories = {
            "classes": self._load_classes,
            "spells": self._load_spells,
            "feats": self._load_generic_list,
            "backgrounds": self._load_generic_list,
            "species": self._load_generic_list,
            "equipment": self._load_generic_list,
            "monsters": self._load_generic_list,
            "modifiers": self._load_generic_list,
            "invocations": self._load_invocations
        }

        for category, loader_func in categories.items():
            dir_path = module_path / category
            if dir_path.exists() or (category == "invocations" and (module_path / "classes").exists()):
               # Invocations might be special, but normally we check if direct dir exists
               # For invocations, we might strictly look into the invocations folder OR scattered.
               # Current logic in service.py was scattered. Let's simplify:
               # If specific loader needs complex logic, it handles the root module path or specific dir
               if category == "invocations":
                    records = loader_func(module_path)
               elif dir_path.exists():
                    records = loader_func(dir_path)
               else:
                    records = []
               
               if records:
                   payload[category] = records

        # Rules
        rules_dir = module_path / "rules"
        if rules_dir.exists():
            payload["rules"] = self._load_rules(rules_dir)

        return payload

    def _load_generic_list(self, directory: Path) -> List[Dict[str, Any]]:
        """Load flat list of records from JSON/MD files."""
        records = []
        for file_path in sorted(list(directory.rglob("*.json")) + list(directory.rglob("*.md"))):
            if file_path.name.startswith("_"): continue
            data = self._read_file(file_path)
            if isinstance(data, dict):
                self._ensure_id(data, file_path)
                data["_meta_source_path"] = str(file_path)
                records.append(data)
        return records

    def _load_spells(self, directory: Path) -> List[Dict[str, Any]]:
        """Load spells, enforcing level directories."""
        records = []
        for level_dir in sorted(directory.iterdir()):
            if not level_dir.is_dir() or not level_dir.name.isdigit():
                continue
            
            level = int(level_dir.name)
            for file_path in sorted(list(level_dir.glob("*.json")) + list(level_dir.glob("*.md"))):
                if file_path.name.startswith("_"): continue
                data = self._read_file(file_path)
                if isinstance(data, dict):
                    self._ensure_id(data, file_path)
                    data["level"] = level # Enforce level matches folder
                    data["_meta_source_path"] = str(file_path)
                    records.append(data)
        return records

    def _load_classes(self, directory: Path) -> List[Dict[str, Any]]:
        """Load classes and their subclasses."""
        records = []
        for entry in sorted(directory.iterdir()):
            if entry.is_dir():
                # Class directory
                base_file = entry / "base.md"
                if not base_file.exists():
                    base_file = entry / "base.json"
                
                if base_file.exists():
                    data = self._read_file(base_file)
                    if isinstance(data, dict):
                        self._ensure_id(data, base_file, default=entry.name)
                        data["_meta_source_path"] = str(base_file)
                        
                        # Load subclasses
                        sub_dir = entry / "subclasses"
                        if sub_dir.exists():
                            data["subclasses"] = self._load_generic_list(sub_dir)

                        # Load options
                        option_dir = entry / "options"
                        if option_dir.exists():
                            option_groups = self._load_generic_list(option_dir)
                            if option_groups:
                                data["options"] = self._merge_option_groups(data.get("options"), option_groups)
                        
                        records.append(data)
            elif entry.is_file() and not entry.name.startswith("_"):
                # Standalone class file
                data = self._read_file(entry)
                if isinstance(data, dict):
                     self._ensure_id(data, entry)
                     data["_meta_source_path"] = str(entry)
                     records.append(data)
        return records
    
    def _merge_option_groups(self, existing: Optional[List[Dict[str, Any]]], additions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        combined: Dict[str, dict] = {}
        ordered_keys: List[str] = []

        def _key(s: str) -> str:
            return s.strip().lower().replace(" ", "_").strip("_")

        def _ingest(items: Iterable[Mapping[str, Any]] | None) -> None:
            if not items:
                return
            for entry in items:
                if not isinstance(entry, dict):
                    continue
                key_value = entry.get("key") or entry.get("name")
                if not isinstance(key_value, str):
                    continue
                key = _key(key_value)
                if key not in combined:
                    ordered_keys.append(key)
                combined[key] = dict(entry)

        _ingest(existing)
        _ingest(additions)
        return [combined[key] for key in ordered_keys]

    
    def _load_invocations(self, module_root: Path) -> List[Dict[str, Any]]:
        """Load invocations from both `invocations/` and `classes/*/invocations/`."""
        records = []
        
        # Top-level invocations
        inv_dir = module_root / "invocations"
        if inv_dir.exists():
            records.extend(self._load_generic_list(inv_dir))
            
        # Class-specific invocations
        classes_dir = module_root / "classes"
        if classes_dir.exists():
             for sub_inv_dir in classes_dir.glob("**/invocations"):
                 if sub_inv_dir.is_dir():
                     records.extend(self._load_generic_list(sub_inv_dir))
        
        return records

    def _load_rules(self, directory: Path) -> Dict[str, Any]:
        """Load nested rules structure."""
        rules = {}
        for file_path in sorted(list(directory.rglob("*.json")) + list(directory.rglob("*.md"))):
            if file_path.name.startswith("_"): continue
            
            key = file_path.relative_to(directory).with_suffix("").as_posix()
            data = self._read_file(file_path)
            if isinstance(data, dict):
                data["_meta_source_path"] = str(file_path)
            rules[key] = data
        return rules

    def _read_file(self, path: Path) -> Any:
        try:
            if path.suffix.lower() == ".json":
                return self._read_json(path)
            elif path.suffix.lower() == ".md":
                return self._read_markdown(path)
        except Exception:
             # Just return empty or log? For now, simplistic
             return {}
        return {}

    def _read_json(self, path: Path) -> Any:
        return json.loads(path.read_text(encoding="utf-8"))

    def _read_markdown(self, path: Path) -> Dict[str, Any]:
        content = path.read_text(encoding="utf-8")
        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                if len(parts) >= 3:
                     data = yaml.safe_load(parts[1]) or {}
                     data["text"] = {"full": parts[2].strip()}
                     
                     if "title" not in data:
                         data["title"] = path.stem.replace("_", " ").title()
                     return data
            except Exception:
                pass
        
        return {
            "title": path.stem.replace("_", " ").title(),
            "text": {"full": content.strip()}
        }

    def _ensure_id(self, data: Dict[str, Any], path: Path, default: Optional[str] = None):
        if "id" not in data:
            data["id"] = default or path.stem

    def _merge_payloads(self, base: Dict[str, Any], overlay: Dict[str, Any]) -> Dict[str, Any]:
        merged = dict(base)
        
        for key, value in overlay.items():
            if key == "rules":
                base_rules = base.get("rules", {})
                merged_rules = dict(base_rules)
                merged_rules.update(value)
                merged["rules"] = merged_rules
            elif isinstance(value, list) and all(isinstance(x, dict) for x in value):
                # Merge lists of records by ID/Name
                base_list = base.get(key, [])
                if not isinstance(base_list, list): base_list = []
                merged[key] = self._merge_record_lists(base_list, value)
            else:
                # specific overrides (like metadata)
                merged[key] = value
                
        return merged

    def _merge_record_lists(self, base: List[Dict[str, Any]], overlay: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # Key by ID
        idx = {self._get_key(r): r for r in base}
        
        for item in overlay:
            key = self._get_key(item)
            idx[key] = item # Overlay replaces base
            
        return list(idx.values())

    def _get_key(self, record: Dict[str, Any]) -> str:
        # Canonical key generation
        rid = record.get("id")
        if rid: return str(rid)
        name = record.get("name")
        if name: return str(name).lower().replace(" ", "_")
        return str(id(record))

