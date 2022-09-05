# QTable Widget
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))

        vbox = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(3)
        table.setItem(0, 0, QTableWidgetItem("Name"))
        table.setItem(0, 1, QTableWidgetItem("Email"))
        table.setItem(0, 2, QTableWidgetItem("Marks"))
        table.setItem(1, 0, QTableWidgetItem("Vaibhav"))
        table.setItem(1, 1, QTableWidgetItem("gulva@sample.com"))
        table.setItem(1, 2, QTableWidgetItem("100"))
        table.setItem(2, 0, QTableWidgetItem("Gullu"))
        table.setItem(2, 1, QTableWidgetItem("gullu@gmail.com"))
        table.setItem(2, 2, QTableWidgetItem("80"))

        vbox.addWidget(table)
        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())