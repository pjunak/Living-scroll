"""Centralized UI theme definitions for Living Scroll.

This module exports the main stylesheet and color palette constants.
Modify this file to update the look and feel of the entire application.
"""

from __future__ import annotations

# --- Color Palette (VSCode-like Dark/Modern) ---
COLORS = {
    # Base
    "bg_main": "#1e1e1e",
    "bg_secondary": "#252526",
    "bg_tertiary": "#2d2d30",
    "bg_input": "#2b2b2b",
    "bg_base": "#121212",       # Deep base (dashboard/hero areas)
    "bg_card": "#1e1e20",       # Card surfaces
    "bg_hero": "qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2b1029, stop:1 #121212)",

    # Text
    "text_primary": "#cccccc",
    "text_secondary": "#999999",
    "text_bright": "#ffffff",
    "text_dim": "#a0a0a0",       # Subdued labels
    "text_muted": "#5f6b7c",     # Very subtle (status text, captions)

    # Accents
    "accent_primary": "#9b59b6",
    "accent_primary_hover": "#8e44ad",
    "accent_hover": "#4e4e4e",
    "accent_dim": "rgba(155, 89, 182, 0.3)",
    "accent_red": "#e74c3c",
    "accent_green": "#27ae60",
    "success": "#2ecc71",         # Brighter green (HP, positive actions)
    "danger": "#e74c3c",          # Alias for accent_red

    # Borders
    "border_dim": "#3e3e42",
    "border_input": "#5d5d5d",
    "border_checkbox": "#888888",
    "border_focus": "#9b59b6",
}

# --- Style Components ---

_CORE_STYLES = f"""
/* Main Window & Backgrounds */
QMainWindow, QWidget {{
    background-color: {COLORS['bg_main']};
    color: {COLORS['text_primary']};
    font-family: "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 10pt;
}}

/* Groups & Frames */
QGroupBox {{
    border: 1px solid {COLORS['border_dim']};
    border-radius: 4px;
    margin-top: 1.2em;
    padding-top: 10px;
    font-weight: 600;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
    color: {COLORS['text_primary']};
}}

/* Header Labels */
QLabel[class="HeaderLabel"] {{
    font-size: 18px;
    font-weight: bold;
    color: {COLORS['accent_primary']};
}}
"""

_INPUT_STYLES = f"""
/* Inputs & Buttons */
QLineEdit, QComboBox, QSpinBox {{
    background-color: {COLORS['bg_input']};
    border: 1px solid {COLORS['border_input']};
    border-radius: 4px;
    padding: 4px 8px;
    color: {COLORS['text_bright']};
}}

QLineEdit:focus, QComboBox:focus, QSpinBox:focus {{
    border: 1px solid {COLORS['border_focus']};
}}

QPushButton, QToolButton {{
    background-color: {COLORS['bg_input']}; 
    border: 1px solid {COLORS['border_dim']};
    border-radius: 4px;
    padding: 5px 10px;
    color: {COLORS['text_primary']};
}}

QPushButton:hover, QToolButton:hover {{
    background-color: {COLORS['accent_hover']};
    border: 1px solid {COLORS['accent_primary']};
}}

QPushButton:pressed, QToolButton:pressed {{
    background-color: {COLORS['accent_primary']};
    color: {COLORS['text_bright']};
}}

/* Primary Action Button */
QPushButton[class="PrimaryButton"] {{
    background-color: {COLORS['accent_primary']};
    color: {COLORS['text_bright']};
    font-weight: bold;
    border: none;
}}

QPushButton[class="PrimaryButton"]:hover {{
    background-color: {COLORS['accent_primary_hover']};
}}

QPushButton[class="PrimaryButton"]:disabled {{
    background-color: #2c3e50;
    color: #7f8c8d;
}}

/* Filter/Toggle Buttons (Checked State) */
QPushButton:checked, QToolButton:checked {{
    background-color: {COLORS['accent_primary']};
    color: {COLORS['text_bright']};
    border: 1px solid {COLORS['accent_primary']};
}}

/* ComboBox Specifics */
QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 0px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}}

QComboBox::down-arrow {{
    width: 0; 
    height: 0; 
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid {COLORS['text_primary']};
    margin-right: 8px;
}}

/* Dropdown list styling */
QComboBox QAbstractItemView {{
    background-color: {COLORS['bg_secondary']};
    border: 1px solid {COLORS['border_dim']};
    selection-background-color: {COLORS['accent_primary']};
    selection-color: {COLORS['text_bright']};
    outline: none;
}}
"""

_CHECKBOX_STYLES = f"""
/* Checkboxes & Radio Buttons */
QCheckBox {{
    spacing: 8px;
    color: {COLORS['text_primary']};
}}

QCheckBox::indicator {{
    width: 14px;
    height: 14px;
    border: 1px solid {COLORS['border_checkbox']}; /* Lighter border */
    border-radius: 2px;
    background: {COLORS['bg_input']};
    margin: 1px;
}}

QCheckBox::indicator:unchecked:hover {{
    border-color: {COLORS['accent_primary']};
}}

QCheckBox::indicator:checked {{
    background-color: {COLORS['accent_primary']};
    border-color: {COLORS['accent_primary']};
    image: url(:/qt-project.org/styles/commonstyle/images/standardbutton-apply-32.png); 
}}

QCheckBox::indicator:checked:hover {{
    background-color: {COLORS['accent_primary_hover']};
    border-color: {COLORS['accent_primary_hover']};
}}

QRadioButton {{
    spacing: 8px;
    color: {COLORS['text_primary']};
}}
QRadioButton::indicator {{
    width: 14px;
    height: 14px;
    border: 1px solid {COLORS['border_checkbox']};
    border-radius: 8px; /* Round */
    background: {COLORS['bg_input']};
}}
QRadioButton::indicator:checked {{
    background-color: {COLORS['accent_primary']};
    border: 4px solid {COLORS['bg_input']}; /* Creates a 'dot' effect */
}}
"""

_SCROLL_LIST_STYLES = f"""
/* Lists, Trees, Tables */
QListWidget, QTreeWidget, QTableView, QTableWidget, QTextBrowser, QScrollArea {{
    background-color: {COLORS['bg_secondary']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 2px;
    outline: none;
}}

QListWidget::item, QTreeWidget::item {{
    padding: 6px;
    border-radius: 2px;
}}

QListWidget::item:hover, QTreeWidget::item:hover, QTableView::item:hover, QTableWidget::item:hover {{
    background-color: {COLORS['accent_primary']}40; /* 25% opacity accent */
}}

QListWidget::item:selected, QTreeWidget::item:selected, QTableView::item:selected, QTableWidget::item:selected {{
    background-color: {COLORS['accent_primary']};
    color: {COLORS['text_bright']};
}}

/* Headers */
QHeaderView::section {{
    background-color: {COLORS['bg_secondary']};
    color: {COLORS['text_primary']};
    padding: 6px;
    border: none;
    border-bottom: 1px solid {COLORS['border_dim']};
    border-right: 1px solid {COLORS['border_dim']};
    font-weight: bold;
}}

/* Indicators (Checkboxes inside lists) */
QListWidget::indicator, QTreeWidget::indicator, QTableView::indicator {{
    width: 14px;
    height: 14px;
    border: 1px solid {COLORS['border_checkbox']};
    border-radius: 2px;
    background: {COLORS['bg_input']};
    margin-right: 4px;
}}

QListWidget::indicator:unchecked:hover, QTreeWidget::indicator:unchecked:hover {{
    border-color: {COLORS['accent_primary']};
}}

QListWidget::indicator:checked, QTreeWidget::indicator:checked {{
    background-color: {COLORS['accent_primary']};
    border-color: {COLORS['accent_primary']};
    image: url(:/qt-project.org/styles/commonstyle/images/standardbutton-apply-32.png);
}}

QListWidget::indicator:checked:hover, QTreeWidget::indicator:checked:hover {{
    background-color: {COLORS['accent_primary_hover']};
    border-color: {COLORS['accent_primary_hover']};
}}
"""

_SCROLLBAR_STYLES = f"""
/* Scrollbars */
QScrollBar:vertical {{
    background: {COLORS['bg_main']};
    width: 12px;
    margin: 0px;
}}

QScrollBar::handle:vertical {{
    background: #424242;
    min-height: 20px;
    border-radius: 6px;
    margin: 2px;
}}

QScrollBar::handle:vertical:hover {{
    background: #4f4f4f;
}}

QScrollBar:horizontal {{
    background: {COLORS['bg_main']};
    height: 12px;
    margin: 0px;
}}

QScrollBar::handle:horizontal {{
    background: #424242;
    min-width: 20px;
    border-radius: 6px;
    margin: 2px;
}}

QScrollBar::add-line, QScrollBar::sub-line {{
    width: 0px; height: 0px;
}}
"""

_TAB_STYLES = f"""
/* TabWidget */
QTabWidget::pane {{
    border: 1px solid {COLORS['border_dim']};
    background-color: {COLORS['bg_main']};
    top: -1px;
}}

QTabBar::tab {{
    background-color: {COLORS['bg_tertiary']};
    color: {COLORS['text_primary']};
    padding: 8px 16px;
    border: 1px solid {COLORS['border_dim']};
    border-bottom: none;
    margin-right: 2px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}}

QTabBar::tab:selected {{
    background-color: {COLORS['bg_main']};
    border-bottom: 1px solid {COLORS['bg_main']};
    color: {COLORS['accent_primary']}; /* Purple text for selected tab */
    font-weight: bold;
}}

QTabBar::tab:hover:!selected {{
    background-color: {COLORS['bg_input']};
}}
"""

_CUSTOM_WIDGET_STYLES = f"""
/* Custom Title Bar */
QWidget#CustomTitleBar {{
    background-color: {COLORS['bg_secondary']};
    border-bottom: 2px solid {COLORS['accent_primary']}; /* Purple Line under title bar */
}}

QLabel#TitleBarLabel {{
    color: {COLORS['text_primary']};
    font-weight: bold;
    border: none;
}}

/* Window Control Buttons */
QPushButton[class="TitleBarButton"], QPushButton[class="TitleBarCloseButton"] {{
    background-color: transparent;
    border: none;
    color: {COLORS['text_primary']};
    border-radius: 0;
}}

QPushButton[class="TitleBarButton"]:hover {{
    background-color: {COLORS['bg_input']};
}}

QPushButton[class="TitleBarCloseButton"]:hover {{
    background-color: {COLORS['accent_red']};
    color: {COLORS['text_bright']};
}}

/* Launcher Tiles */
QPushButton[class="TileButton"] {{
    background-color: {COLORS['bg_secondary']};
    color: {COLORS['text_primary']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 6px;
    text-align: left;
    padding: 20px;
    font-size: 18px;
    font-weight: 600;
}}

QPushButton[class="TileButton"]:hover {{
    background-color: {COLORS['bg_tertiary']};
    border: 1px solid {COLORS['accent_primary']}; /* Purple border on hover */
}}

QPushButton[class="TileButton"]:pressed {{
    background-color: {COLORS['accent_primary']};
    color: {COLORS['text_bright']};
}}

/* Character Tile (Selector) */
QFrame[class="CharacterTile"] {{
    background-color: {COLORS['bg_secondary']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 12px;
}}
QFrame[class="CharacterTile"]:hover {{
    background-color: {COLORS['bg_tertiary']};
    border-color: {COLORS['accent_primary']};
}}
QFrame[class="CharacterTile"][isSelected="true"] {{
    border: 2px solid {COLORS['accent_primary']};
    background-color: {COLORS['bg_main']};
}}

/* Character Portrait */
QLabel[class="CharacterPortrait"] {{
    background-color: {COLORS['bg_tertiary']};
    border: 2px solid {COLORS['border_dim']};
    border-radius: 8px; /* Slightly rounded squares */
}}
QLabel[class="CharacterPortrait"]:hover {{
    border-color: {COLORS['accent_primary']};
}}

/* Utility Labels */
QLabel[class="DimLabel"] {{
    color: {COLORS['text_secondary']};
    font-style: italic;
}}

QLabel[class="StatusLabel"] {{
    color: #7f8c8d;
    font-size: 11px;
}}

QLabel[class="SectionTitle"] {{
    font-weight: 700;
    font-size: 14px;
    color: {COLORS['text_bright']};
    margin-top: 8px;
    margin-bottom: 4px;
}}

/* Stat Displays */
QLabel[class="ValueLabel"] {{
    font-size: 24px;
    font-weight: 800;
    color: {COLORS['text_bright']};
}}

QLabel[class="LabelLabel"] {{
    font-size: 11px;
    font-weight: 700;
    color: {COLORS['text_secondary']};
    text-transform: uppercase;
}}

/* Subtle Action Button (like Open Source) */
QPushButton[class="SubtleButton"] {{
    background-color: transparent;
    border: none;
    color: {COLORS['text_secondary']};
    text-align: left;
    padding: 6px;
}}
QPushButton[class="SubtleButton"]:hover {{
    background-color: {COLORS['bg_input']};
    color: {COLORS['text_bright']};
}}

/* Badges / Tags */
QLabel[class="BadgeLabel"] {{
    background-color: {COLORS['bg_input']};
    color: {COLORS['text_primary']};
    border: 1px solid {COLORS['border_input']};
    border-radius: 6px;
    padding: 4px 8px;
    font-weight: 600;
    font-size: 11px;
}}

/* Info/Selection Box (Transparent with border) */
QLabel[class="InfoBorder"] {{
    background-color: transparent;
    border: 1px solid {COLORS['border_dim']};
    border-radius: 8px;
    padding: 12px;
}}
/* Character Builder Level Entry */
QFrame[class="LevelEntry"] {{
    background-color: {COLORS['bg_secondary']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 4px;
    margin-bottom: 8px;
}}
QFrame[class="LevelEntryBody"] {{
    border-left: 2px solid {COLORS['accent_primary']};
    margin-left: 8px;
    padding-left: 10px;
}}
QPushButton[class="DestructiveButton"] {{
    background-color: transparent;
    color: {COLORS['accent_red']};
    border: none;
    font-weight: bold;
    padding: 2px 6px;
}}
QPushButton[class="DestructiveButton"]:hover {{
    color: #ff6b6b;
    background-color: {COLORS['bg_tertiary']};
}}

/* Typography Overrides */
QLabel[class="BoldLabel"] {{
    font-weight: bold;
}}
QLabel[class="MutedItalicLabel"] {{
    color: {COLORS['text_secondary']};
    font-style: italic;
    font-size: 0.9em;
}}
QLabel[class="WarningItalicLabel"] {{
    color: {COLORS['accent_red']};
    font-style: italic;
}}
QLabel[class="SuccessItalicLabel"] {{
    color: {COLORS['accent_green']};
    font-style: italic;
}}
QLabel[class="SuccessBoldLabel"] {{
    color: {COLORS['accent_green']};
    font-weight: bold;
}}

/* Build Portrait */
QLabel[class="BuildPortrait"] {{
    background-color: {COLORS['bg_tertiary']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 4px;
}}
"""

_REUSABLE_WIDGET_STYLES = f"""
/* ── Stat Box ───────────────────────────────────────────── */
QFrame[class="StatBox"] {{
    background-color: {COLORS['bg_card']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 8px;
    padding: 8px;
}}
QLabel[class="StatBoxValue"] {{
    font-weight: 900;
    color: {COLORS['text_bright']};
}}
QLabel[class="StatBoxLabel"] {{
    font-weight: 700;
    color: {COLORS['text_dim']};
    text-transform: uppercase;
}}

/* Size variants via dynamic property "size" */
QFrame[class="StatBox"][size="small"] {{ min-width: 48px; max-width: 72px; }}
QFrame[class="StatBox"][size="medium"] {{ min-width: 72px; max-width: 110px; }}
QFrame[class="StatBox"][size="large"] {{ min-width: 110px; max-width: 160px; }}

QFrame[class="StatBox"][size="small"] QLabel[class="StatBoxValue"] {{ font-size: 18px; }}
QFrame[class="StatBox"][size="medium"] QLabel[class="StatBoxValue"] {{ font-size: 28px; }}
QFrame[class="StatBox"][size="large"] QLabel[class="StatBoxValue"] {{ font-size: 36px; }}

QFrame[class="StatBox"][size="small"] QLabel[class="StatBoxLabel"] {{ font-size: 8px; }}
QFrame[class="StatBox"][size="medium"] QLabel[class="StatBoxLabel"] {{ font-size: 10px; }}
QFrame[class="StatBox"][size="large"] QLabel[class="StatBoxLabel"] {{ font-size: 12px; }}

/* ── Adjustment Control (+/−) ──────────────────────────── */
QPushButton[class="AdjustMinus"] {{
    background-color: transparent;
    color: {COLORS['danger']};
    border: 2px solid {COLORS['danger']};
    border-radius: 13px;
    font-weight: 900;
    font-size: 16px;
    min-width: 26px;
    max-width: 26px;
    min-height: 26px;
    max-height: 26px;
    padding: 0px;
}}
QPushButton[class="AdjustMinus"]:hover {{
    background-color: rgba(231, 76, 60, 0.2);
}}
QPushButton[class="AdjustMinus"]:pressed {{
    background-color: {COLORS['danger']};
    color: {COLORS['text_bright']};
}}

QPushButton[class="AdjustPlus"] {{
    background-color: transparent;
    color: {COLORS['success']};
    border: 2px solid {COLORS['success']};
    border-radius: 13px;
    font-weight: 900;
    font-size: 16px;
    min-width: 26px;
    max-width: 26px;
    min-height: 26px;
    max-height: 26px;
    padding: 0px;
}}
QPushButton[class="AdjustPlus"]:hover {{
    background-color: rgba(46, 204, 113, 0.2);
}}
QPushButton[class="AdjustPlus"]:pressed {{
    background-color: {COLORS['success']};
    color: {COLORS['text_bright']};
}}

QLabel[class="AdjustValue"] {{
    font-size: 24px;
    font-weight: 900;
    color: {COLORS['success']};
    min-width: 50px;
    qproperty-alignment: AlignCenter;
}}

/* ── Circular Button (icon action) ─────────────────────── */
QPushButton[class="CircularButton"] {{
    background-color: transparent;
    border: 2px solid {COLORS['border_dim']};
    border-radius: 15px;
    min-width: 30px;
    max-width: 30px;
    min-height: 30px;
    max-height: 30px;
    padding: 0px;
    color: {COLORS['text_primary']};
}}
QPushButton[class="CircularButton"]:hover {{
    border-color: {COLORS['accent_primary']};
    background-color: {COLORS['accent_dim']};
}}

/* ── Filter Toggle ─────────────────────────────────────── */
QPushButton[class="FilterToggle"] {{
    background-color: transparent;
    border: 1px solid {COLORS['border_dim']};
    border-radius: 4px;
    padding: 4px 8px;
    font-weight: bold;
    color: {COLORS['text_primary']};
}}
QPushButton[class="FilterToggle"]:checked {{
    color: {COLORS['text_bright']};
}}
QPushButton[class="FilterToggle"]:hover {{
    border-color: {COLORS['accent_primary']};
}}

/* ── Section Card ──────────────────────────────────────── */
QFrame[class="SectionCard"] {{
    background-color: {COLORS['bg_secondary']};
    border: 1px solid {COLORS['border_dim']};
    border-radius: 8px;
    padding: 12px;
}}
QLabel[class="SectionCardTitle"] {{
    font-weight: 700;
    font-size: 14px;
    color: {COLORS['accent_primary']};
    margin-bottom: 6px;
}}
"""

# Combine all blocks
DARK_THEME_STYLESHEET = "\n".join([
    _CORE_STYLES,
    _INPUT_STYLES,
    _CHECKBOX_STYLES,
    _SCROLL_LIST_STYLES,
    _SCROLLBAR_STYLES,
    _TAB_STYLES,
    _CUSTOM_WIDGET_STYLES,
    _REUSABLE_WIDGET_STYLES,
])

__all__ = ["DARK_THEME_STYLESHEET", "COLORS"]
