# QLabel Widget
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,400)
        self.setWindowTitle("Python GUI App")
        self.setWindowIcon(QIcon("images/python.png"))
        #self.setStyleSheet('background-color: green')
        #self.setWindowOpacity(0.8)
        #self.setFixedWidth(700)
        #self.setFixedHeight(400) 

        label = QLabel(self)
        label.setText("My new Label")
        label.move(400, 100)
        label.setFont(QFont('Comic Sans MS', 20))
        #label.setNum(10)
        #label.clear()

        label_2 = QLabel(self)
        pixmap = QPixmap('images/python.png')
        label_2.setPixmap(pixmap)

        label_3 = QLabel(self)
        label.move(400, 100)
        movie = QMovie('images/minion.gif')
        label_3.setMovie(movie)
        movie.setSpeed(100)
        movie.start()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())