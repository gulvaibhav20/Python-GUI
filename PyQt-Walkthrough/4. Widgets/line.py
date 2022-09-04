# QLine Widget
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Rockwell", 20))
        #line_edit.setText("Default text")
        line_edit.setPlaceholderText("Please enter your username")
        #line_edit.setEnabled(False) # To disable the line edit
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())