from PySide6.QtWidgets import QApplication
from modules.dashboard.ui.window import DashboardWindow
import sys, time

app = QApplication(sys.argv)
win = DashboardWindow()
win.show()

# Open char builder
win._current_view.open_builder()

time.sleep(2)
# Click around or select something
from modules.character_sheet.ui.builder.dialog import CharacterBuilderDialog

# find top level dialog
for widget in app.topLevelWidgets():
    if isinstance(widget, CharacterBuilderDialog):
        builder = widget
        break

time.sleep(1)
builder.reject()
win.close()
