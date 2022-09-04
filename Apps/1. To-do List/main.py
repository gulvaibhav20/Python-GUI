from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont

class Ui_Form(object):
    def setupUi(self, Form):
        self.count = 1
        Form.setObjectName("Form")
        Form.resize(800, 600)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 721, 571))
        self.widget.setObjectName("widget")
        self.main_vertical = QtWidgets.QVBoxLayout(self.widget)
        self.main_vertical.setContentsMargins(0, 0, 0, 0)
        self.main_vertical.setObjectName("main_vertical")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.task)
        self.btn.setStyleSheet('background-color: pink; color: purple')
        self.horizontalLayout.addWidget(self.btn)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.main_vertical.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label.setStyleSheet('background-color: lightgreen; color: purple')
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_1 = QtWidgets.QVBoxLayout()
        self.list_1.setObjectName("list_1")
        self.horizontalLayout_2.addLayout(self.list_1)
        self.list_2 = QtWidgets.QVBoxLayout()
        self.list_2.setObjectName("list_2")
        self.horizontalLayout_2.addLayout(self.list_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.main_vertical.addLayout(self.verticalLayout)
        self.verticalLayout.addStretch(10)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "To-do List"))
        self.btn.setText(_translate("Form", "Add Task"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter your Task"))
        self.label.setText(_translate("Form", "Your Task List"))

    def task(self):
        text = self.lineEdit.text()
        if(text != ''):
            self.text_label = QLabel(text)
            self.text_label.setFont(QFont("Rockwell", 14))
            self.bullet_label = QLabel(str(self.count) + ".")
            self.bullet_label.setFont(QFont("Rockwell", 14))
            self.list_1.addWidget(self.bullet_label)
            self.list_2.addWidget(self.text_label)
            self.lineEdit.clear()
            self.count += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
