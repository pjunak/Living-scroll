"""Reusable StatBox widget — large value + small label."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class StatBox(QFrame):
    """
    Compact stat display: a prominent numeric value over a small label.

    Uses ``StatBox``, ``StatBoxValue``, and ``StatBoxLabel`` QSS classes
    from the global theme.  The ``size`` property ("small", "medium",
    "large") controls font scaling via QSS.

    Parameters
    ----------
    value : str | int
        The display value (e.g. "14" or "+2").
    label : str
        Caption below the value (e.g. "AC", "SPEED").
    size : str
        One of "small", "medium", "large".  Controls width and font size.
    color : str | None
        Optional inline color override for the value label.
    parent : QWidget | None
        Parent widget.
    """

    def __init__(
        self,
        value: str | int = "—",
        label: str = "",
        *,
        size: str = "medium",
        color: str | None = None,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self.setProperty("class", "StatBox")
        self.setProperty("size", size)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._value_label = QLabel(str(value))
        self._value_label.setProperty("class", "StatBoxValue")
        self._value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if color:
            self._value_label.setStyleSheet(f"color: {color};")

        self._text_label = QLabel(label.upper())
        self._text_label.setProperty("class", "StatBoxLabel")
        self._text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self._value_label)
        layout.addWidget(self._text_label)

    # ── Public API ────────────────────────────────────────────────

    def set_value(self, value: str | int) -> None:
        self._value_label.setText(str(value))

    def set_label(self, label: str) -> None:
        self._text_label.setText(label.upper())

    def set_color(self, color: str) -> None:
        self._value_label.setStyleSheet(f"color: {color};")
