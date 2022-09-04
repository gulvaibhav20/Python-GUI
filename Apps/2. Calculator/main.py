from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEdit_first = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_first.setFont(font)
        self.lineEdit_first.setMouseTracking(True)
        self.lineEdit_first.setObjectName("lineEdit_first")
        self.horizontalLayout_2.addWidget(self.lineEdit_first)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineEdit_second = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_second.setFont(font)
        self.lineEdit_second.setMouseTracking(True)
        self.lineEdit_second.setObjectName("lineEdit_second")
        self.horizontalLayout_3.addWidget(self.lineEdit_second)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_subtract = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btn_subtract.setFont(font)
        self.btn_subtract.setObjectName("btn_subtract")
        self.btn_subtract.clicked.connect(self.subtract)
        self.horizontalLayout.addWidget(self.btn_subtract)
        self.btn_multiply = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_multiply.clicked.connect(self.multiply)
        self.horizontalLayout.addWidget(self.btn_multiply)
        self.btn_divide = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.btn_divide.setFont(font)
        self.btn_divide.setObjectName("btn_divide")
        self.btn_divide.clicked.connect(self.divide)
        self.horizontalLayout.addWidget(self.btn_divide)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("QLabel{\n"
"    color: green;\n"
"}")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add(self):
        fnum = int(self.lineEdit_first.text())
        snum = int(self.lineEdit_second.text())
        self.result.setText("Result :" + str(fnum + snum))

    def subtract(self):
        fnum = int(self.lineEdit_first.text())
        snum = int(self.lineEdit_second.text())
        self.result.setText("Result :" + str(fnum - snum))

    def multiply(self):
        fnum = int(self.lineEdit_first.text())
        snum = int(self.lineEdit_second.text())
        self.result.setText("Result :" + str(fnum * snum))

    def divide(self):
        fnum = int(self.lineEdit_first.text())
        snum = int(self.lineEdit_second.text())
        self.result.setText("Result :" + str(fnum / snum))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Number:"))
        self.label_2.setText(_translate("Form", "Second Number:"))
        self.btn_add.setText(_translate("Form", "Add"))
        self.btn_subtract.setText(_translate("Form", "Subtract"))
        self.btn_multiply.setText(_translate("Form", "Multiply"))
        self.btn_divide.setText(_translate("Form", "Divide"))
        self.result.setText(_translate("Form", "Result:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())