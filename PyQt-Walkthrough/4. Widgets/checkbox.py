# Checkbox
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,300,200)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))

        hbox = QHBoxLayout()
        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QIcon("images/py.png"))
        self.check1.setIconSize(QSize(40,40))
        self.check1.setFont(QFont("Poor Richard", 15))
        self.check1.stateChanged.connect(self.item_selected)
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QIcon("images/java.png"))
        self.check2.setIconSize(QSize(40,40))
        self.check2.setFont(QFont("Poor Richard", 15))
        self.check2.stateChanged.connect(self.item_selected)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("Javascript")
        self.check3.setIcon(QIcon("images/javascript.png"))
        self.check3.setIconSize(QSize(40,40))
        self.check3.setFont(QFont("Poor Richard", 15))
        self.check3.stateChanged.connect(self.item_selected)
        hbox.addWidget(self.check3)

        self.label = QLabel("Result")
        self.label.setFont(QFont("Poor Richard", 15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def item_selected(self):
        value = ""
        if self.check1.isChecked():
            value = self.check1.text()
        if self.check2.isChecked():
            value = self.check2.text()
        if self.check3.isChecked():
            value = self.check3.text()
        
        self.label.setText("You have selected :" + value)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())