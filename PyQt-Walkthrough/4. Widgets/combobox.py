# QComboBox Widget
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()
        label = QLabel("Select Account Type: ")
        label.setFont(QFont("Times", 15))
        self.combo = QComboBox()
        self.combo.addItem("Current Account")
        self.combo.addItem("Deposit Account")
        self.combo.addItem("Savings Account")
        self.combo.addItem("Salary Account")
        self.combo.currentIndexChanged.connect(self.combo_changed)
        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        vbox = QVBoxLayout()
        self.result = QLabel()
        self.result.setFont(QFont("Times", 15))
        vbox.addLayout(hbox)
        vbox.addWidget(self.result)
        
        self.setLayout(vbox)
    
    def combo_changed(self):
        item = self.combo.currentText()
        self.result.setText("Your account type : " + item)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())