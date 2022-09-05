# QSlider Widget
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,100)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        vbox = QVBoxLayout()

        self.label = QLabel("Slider Program")
        self.label.setFont(QFont("Rockwell", 20))
        vbox.addWidget(self.label)

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changed_slider)
        vbox.addWidget(self.slider)

        self.line = QLineEdit()
        self.line.setFont(QFont("Times", 15))
        self.line.returnPressed.connect(self.line_changed)
        vbox.addWidget(self.line)

        vbox.addStretch(20)
        self.setLayout(vbox)

    def changed_slider(self):
        value = self.slider.value()
        self.line.setText(str(value))

    def line_changed(self):
        value = int(self.line.text())
        self.slider.setValue(value)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())