# QPushButton Widget
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        self.create_btn()

    def create_btn(self):
        btn = QPushButton("Click Here", self)
        btn.setGeometry(100,100,300,100)
        btn.setFont(QFont("Rockwell", 20, QFont.Weight.Bold))
        btn.setIcon(QIcon('images/python.png'))
        btn.setIconSize(QSize(50,50))
        btn.setStyleSheet('background-color: pink; color: purple')

        # Pop-up menu
        menu = QMenu()
        menu.setFont(QFont("Rockwell", 15))
        menu.setStyleSheet('background-color: green')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())