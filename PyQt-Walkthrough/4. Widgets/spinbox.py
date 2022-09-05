# SpinBox Example
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QSpinBox, QDoubleSpinBox
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))

        hbox1 = QHBoxLayout()
        self.label = QLabel("Laptop Price")
        self.label.setFont(QFont("Rockwell", 15))
        self.line1 = QLineEdit()
        self.line1.setPlaceholderText("Enter Laptop Price")
        self.spinbox = QSpinBox()
        self.spinbox.editingFinished.connect(self.laptop_price)
        self.line2 = QLineEdit()
        hbox1.addWidget(self.label)
        hbox1.addWidget(self.line1)
        hbox1.addWidget(self.spinbox)
        hbox1.addWidget(self.line2)

        hbox2 = QHBoxLayout()
        self.label2 = QLabel("Book Price")
        self.label2.setFont(QFont("Rockwell", 15))
        self.line3 = QLineEdit()
        self.line3.setPlaceholderText("Enter Book Price")
        self.spinbox2 = QDoubleSpinBox()
        self.spinbox2.editingFinished.connect(self.total_price)
        self.line4 = QLineEdit()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.line3)
        hbox2.addWidget(self.spinbox2)
        hbox2.addWidget(self.line4)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.result = QLabel()
        self.result.setFont(QFont("Times New Roman", 20))
        vbox.addWidget(self.result)
        vbox.addStretch(50)
        self.setLayout(vbox)
    
    def laptop_price(self):
        if self.line1.text() != '' and self.line1.text() != '0':
            price = int(self.line1.text())
            total = price * self.spinbox.value()
            self.line2.setText(str(total))

    def total_price(self):
        if self.line3.text() != '' and self.line3.text() != '0':
            price = float(self.line3.text())
            total = price * self.spinbox2.value()
            self.line4.setText(str(total))
            laptop = float(self.line2.text())
            total += laptop
            self.result.setText("Total Price : " + str(total))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())