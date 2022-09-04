# Radio Button
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,300,200)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()
        rad1 = QRadioButton("Python")
        rad1.setIcon(QIcon("images/py.png"))
        rad1.setIconSize(QSize(40,40))
        rad1.setFont(QFont("Rockwell", 20))
        rad1.setChecked(True)
        rad1.toggled.connect(self.radio_select)

        rad2 = QRadioButton("Java")
        rad2.setIcon(QIcon("images/java.png"))
        rad2.setIconSize(QSize(40,40))
        rad2.setFont(QFont("Rockwell", 20))
        rad2.toggled.connect(self.radio_select)

        rad3 = QRadioButton("JavaScript")
        rad3.setIcon(QIcon("images/javascript.png"))
        rad3.setIconSize(QSize(40,40))
        rad3.setFont(QFont("Rockwell", 20))
        rad3.toggled.connect(self.radio_select)

        self.label = QLabel("Tech Used : Python")
        self.label.setFont(QFont("Sanserif", 20))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        hbox.addWidget(rad3)
        self.setLayout(vbox)

    def radio_select(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText("Tech Used : " + radio_btn.text())

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())