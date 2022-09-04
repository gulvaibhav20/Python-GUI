# Event Handling
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        self.label = QLabel("Default Text")
        btn.clicked.connect(self.clicked_btn)
        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Rockwell", 15))
        self.label.setStyleSheet('color: red')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())