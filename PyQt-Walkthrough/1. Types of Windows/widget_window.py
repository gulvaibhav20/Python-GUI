# QWidget Window Example
from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
#window.statusBar().showMessage("Welcome to my App") - It will give us an error.
window.show()
sys.exit(app.exec())