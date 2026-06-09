"""
Management entry tab – one standalone tab per management YAML entry.

Each class/subclass/feat can define ``management`` entries in its YAML.
The dialog creates one tab per entry, using the entry's ``label`` as the
tab name.  State is persisted via ``CharacterData.management_state``.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from modules.character_sheet.model import CharacterSheet
from modules.character_sheet.model.schema import CharacterData
from modules.compendium.service import Compendium

log = logging.getLogger(__name__)


# ─── Public helper: collect all management entries ─────────────────

def collect_management_entries(
    sheet: CharacterSheet,
    compendium: Compendium,
) -> List[Dict[str, Any]]:
    """
    Return a flat list of management descriptors from every class AND
    subclass the character has.  Each dict is the raw YAML entry
    augmented with:
      - ``_class_name``  : owning class
      - ``_class_level`` : current class level
      - ``_state_key``   : unique key for CharacterData.management_state
      - ``_tab_label``   : display name for the tab (disambiguated)
    """
    # Collect raw (label, source_name, cls, entry) tuples from all sources
    raw_items: List[tuple] = []
    classes = getattr(sheet.identity, "classes", [])

    for cls in classes:
        # Base class management entries
        record = compendium.class_record(cls.name)
        if record:
            for raw in record.get("management", []) or []:
                if isinstance(raw, dict) and "id" in raw:
                    raw_items.append((cls.name, cls, raw))

        # Subclass management entries
        subclass_name = getattr(cls, "subclass", None)
        if subclass_name and record:
            sub_record = compendium.subclass_record(cls.name, subclass_name)
            if sub_record:
                for raw in sub_record.get("management", []) or []:
                    if isinstance(raw, dict) and "id" in raw:
                        raw_items.append((cls.name, cls, raw))

    # Count labels for disambiguation
    label_counts: Dict[str, int] = {}
    for source_name, cls, raw in raw_items:
        label = raw.get("label", raw["id"].replace("_", " ").title())
        label_counts[label] = label_counts.get(label, 0) + 1

    # Build final entries with disambiguation
    entries: List[Dict[str, Any]] = []
    for source_name, cls, raw in raw_items:
        label = raw.get("label", raw["id"].replace("_", " ").title())
        if label_counts.get(label, 0) > 1:
            tab_label = f"{cls.name} — {label}"
        else:
            tab_label = label

        entry = dict(raw)
        entry["_class_name"] = cls.name
        entry["_class_level"] = cls.level
        entry["_state_key"] = f"{cls.name.lower()}:{raw['id']}"
        entry["_tab_label"] = tab_label
        entries.append(entry)

    return entries


# ─── Tab widget (one per management entry) ─────────────────────────

class ManagementEntryTab(QWidget):
    """
    A standalone tab for a single management entry (e.g. Spellbook,
    Prepared Spells, Known Spells, Invocations).
    """

    dataChanged = Signal()

    def __init__(
        self,
        entry: Dict[str, Any],
        sheet: CharacterSheet,
        data: CharacterData,
        compendium: Compendium,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._entry = entry
        self._sheet = sheet
        self._data = data
        self._compendium = compendium

        self._state_key: str = entry["_state_key"]
        self._items: List[str] = list(data.management_state.get(self._state_key, []))

        self._build_ui()

    # ── Layout ────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(12)

        mgmt_type = self._entry.get("type", "")

        # ── Header ────────────────────────────────────────────────
        class_name = self._entry.get("_class_name", "")
        label = self._entry.get("label", "")
        header = QLabel(f"{class_name} — {label}")
        header.setProperty("class", "HeaderLabel")
        layout.addWidget(header)

        # ── Description ───────────────────────────────────────────
        desc = self._entry.get("description", "")
        if desc:
            desc_lbl = QLabel(desc)
            desc_lbl.setWordWrap(True)
            desc_lbl.setProperty("class", "DimLabel")
            layout.addWidget(desc_lbl)

        # ── Status / cap ──────────────────────────────────────────
        self._status_label = QLabel()
        self._status_label.setProperty("class", "StatusLabel")
        layout.addWidget(self._status_label)

        # ── Item list ─────────────────────────────────────────────
        self._list = QListWidget()
        self._list.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self._populate_list()
        layout.addWidget(self._list)

        # ── Action buttons ────────────────────────────────────────
        btn_row = QHBoxLayout()
        btn_row.setSpacing(8)

        if mgmt_type in ("spell_collection", "spell_preparation", "spell_known"):
            add_btn = QPushButton("Add Spell…")
            add_btn.setProperty("class", "PrimaryButton")
            add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            add_btn.clicked.connect(self._on_add_spell)
            btn_row.addWidget(add_btn)
        elif mgmt_type == "feature_selection":
            add_btn = QPushButton("Add Feature…")
            add_btn.setProperty("class", "PrimaryButton")
            add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            add_btn.clicked.connect(self._on_add_feature)
            btn_row.addWidget(add_btn)

        remove_btn = QPushButton("Remove Selected")
        remove_btn.setProperty("class", "DestructiveButton")
        remove_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        remove_btn.clicked.connect(self._on_remove)
        btn_row.addWidget(remove_btn)

        btn_row.addStretch()
        layout.addLayout(btn_row)

        layout.addStretch()
        scroll.setWidget(content)
        root.addWidget(scroll)

        self._update_status()

    # ── List helpers ──────────────────────────────────────────────

    def _populate_list(self) -> None:
        self._list.clear()
        for name in self._items:
            item = QListWidgetItem(name)
            item.setData(Qt.ItemDataRole.UserRole, name)
            self._list.addItem(item)

    def _update_status(self) -> None:
        count = len(self._items)
        max_str = self._compute_max()
        if max_str is not None:
            self._status_label.setText(f"{count} / {max_str} selected")
        else:
            self._status_label.setText(f"{count} item(s)")

    def _compute_max(self) -> str | None:
        formula = self._entry.get("max_formula")
        if not formula:
            return None
        try:
            from modules.character_sheet.services.formula import evaluate_formula
            result = evaluate_formula(formula, self._sheet)
            return str(max(1, result))
        except Exception as exc:
            log.warning("Could not evaluate formula %r: %s", formula, exc)
            return "?"

    def _persist(self) -> None:
        """Write current items back to CharacterData."""
        self._data.management_state[self._state_key] = list(self._items)
        self.dataChanged.emit()

    # ── Slots ─────────────────────────────────────────────────────

    def _on_add_spell(self) -> None:
        try:
            from modules.grimoire.ui.window import SpellWindow
            picker = SpellWindow(parent=self, selection_mode=True)

            def _on_selected(payload: dict) -> None:
                name = payload.get("name", "")
                if not name or name in self._items:
                    return
                self._items.append(name)
                self._populate_list()
                self._update_status()
                self._persist()

            picker.item_selected.connect(_on_selected)
            picker.show()
        except Exception as exc:
            log.error("Failed to open spell picker: %s", exc)

    def _on_add_feature(self) -> None:
        # Placeholder for feature_selection pickers (invocations, maneuvers)
        log.info("Feature picker not yet implemented for %s", self._state_key)

    def _on_remove(self) -> None:
        selected = self._list.selectedItems()
        if not selected:
            return
        for item in selected:
            name = item.data(Qt.ItemDataRole.UserRole)
            if name in self._items:
                self._items.remove(name)
        self._populate_list()
        self._update_status()
        self._persist()
