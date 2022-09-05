# QListWidget Widget
from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()
        self.list = QListWidget()
        self.list.insertItem(0, "Python")
        self.list.insertItem(1, "Java")
        self.list.insertItem(2, "C++")
        self.list.insertItem(3, "C#")
        self.list.insertItem(4, "Kotlin")
        self.list.clicked.connect(self.select_item)
        self.list.currentItemChanged.connect(self.select_item)
        vbox.addWidget(self.list)

        self.result = QLabel()
        self.result.setFont(QFont("Rockwell", 15))
        vbox.addWidget(self.result)
        self.setLayout(vbox)

    def select_item(self):
        item = self.list.currentItem()
        self.result.setText("You have selected : " + str(item.text()))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())