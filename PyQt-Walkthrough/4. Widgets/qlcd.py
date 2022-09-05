# QLCDNumber Example
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))

        # Timer functionality
        timer = QTimer()
        timer.timeout.connect(self.show_lcd)
        timer.start(1000) # value in miliseconds
        self.show_lcd()

    def show_lcd(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet('background-color: red')
        vbox.addWidget(lcd)
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        lcd.display(text)
        self.setLayout(vbox)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())