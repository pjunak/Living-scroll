"""Reusable SectionCard widget — bordered rounded frame with optional title."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class SectionCard(QFrame):
    """
    Bordered, rounded card container with an optional accent title.

    Uses ``SectionCard`` and ``SectionCardTitle`` QSS classes from the
    global theme.

    Parameters
    ----------
    title : str | None
        Optional card header text (rendered in accent color).
    parent : QWidget | None
        Parent widget.
    """

    def __init__(self, title: str | None = None, *, parent=None) -> None:
        super().__init__(parent)
        self.setProperty("class", "SectionCard")

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(12, 12, 12, 12)
        self._layout.setSpacing(8)

        self._title_label: QLabel | None = None
        if title:
            self._title_label = QLabel(title)
            self._title_label.setProperty("class", "SectionCardTitle")
            self._layout.addWidget(self._title_label)

    # ── Public API ────────────────────────────────────────────────

    def add_widget(self, widget: QWidget) -> None:
        """Add a child widget to the card's content area."""
        self._layout.addWidget(widget)

    def add_layout(self, layout) -> None:
        """Add a child layout to the card's content area."""
        self._layout.addLayout(layout)

    def set_title(self, title: str) -> None:
        if self._title_label:
            self._title_label.setText(title)
        else:
            self._title_label = QLabel(title)
            self._title_label.setProperty("class", "SectionCardTitle")
            self._layout.insertWidget(0, self._title_label)

    def content_layout(self) -> QVBoxLayout:
        """Return the internal layout for direct manipulation."""
        return self._layout
