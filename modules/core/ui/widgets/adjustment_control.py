"""Reusable +/− adjustment control widget."""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget


class AdjustmentControl(QWidget):
    """
    Horizontal widget: [ − ]  value  [ + ]

    Emits ``value_changed(int)`` when the user clicks + or −.

    Uses ``AdjustMinus``, ``AdjustPlus``, and ``AdjustValue`` QSS
    classes from the global theme.

    Parameters
    ----------
    value : int
        Initial display value.
    min_val : int | None
        Minimum bound (inclusive).  ``None`` = no minimum.
    max_val : int | None
        Maximum bound (inclusive).  ``None`` = no maximum.
    step : int
        Amount to increment / decrement per click.
    parent : QWidget | None
        Parent widget.
    """

    value_changed = Signal(int)

    def __init__(
        self,
        value: int = 0,
        *,
        min_val: int | None = None,
        max_val: int | None = None,
        step: int = 1,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self._value = value
        self._min = min_val
        self._max = max_val
        self._step = step

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._btn_minus = QPushButton("−")
        self._btn_minus.setProperty("class", "AdjustMinus")
        self._btn_minus.setFixedSize(26, 26)
        self._btn_minus.setCursor(Qt.CursorShape.PointingHandCursor)
        self._btn_minus.clicked.connect(self._decrement)

        self._display = QLabel(str(value))
        self._display.setProperty("class", "AdjustValue")
        self._display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._btn_plus = QPushButton("+")
        self._btn_plus.setProperty("class", "AdjustPlus")
        self._btn_plus.setFixedSize(26, 26)
        self._btn_plus.setCursor(Qt.CursorShape.PointingHandCursor)
        self._btn_plus.clicked.connect(self._increment)

        layout.addWidget(self._btn_minus)
        layout.addWidget(self._display)
        layout.addWidget(self._btn_plus)

    # ── Public API ────────────────────────────────────────────────

    @property
    def value(self) -> int:
        return self._value

    def set_value(self, v: int) -> None:
        self._value = v
        self._display.setText(str(v))

    def set_display_color(self, color: str) -> None:
        """Override the display label color (e.g. red when HP is low)."""
        self._display.setStyleSheet(f"color: {color};")

    # ── Slots ─────────────────────────────────────────────────────

    def _decrement(self) -> None:
        new = self._value - self._step
        if self._min is not None and new < self._min:
            return
        self._value = new
        self._display.setText(str(new))
        self.value_changed.emit(new)

    def _increment(self) -> None:
        new = self._value + self._step
        if self._max is not None and new > self._max:
            return
        self._value = new
        self._display.setText(str(new))
        self.value_changed.emit(new)
