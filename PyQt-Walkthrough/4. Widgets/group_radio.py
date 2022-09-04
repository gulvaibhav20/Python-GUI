from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet("QLabel{\n"
"    color: purple\n"
"}\n"
"")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(10, 330, 52, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.label_result.setFixedWidth(590)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 212, 135))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_1 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_1.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_2.toggled.connect(self.radio_selected)
        
        self.verticalLayout.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_3.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.btn_3)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 170, 352, 135))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.btn_4 = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_4.toggled.connect(self.radio_selected)
        
        self.verticalLayout_2.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_5.toggled.connect(self.radio_selected)

        self.verticalLayout_2.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_6.toggled.connect(self.radio_selected)

        self.verticalLayout_2.addWidget(self.btn_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radio_selected(self):
        selected1 = ""
        selected2 = ""

        if self.btn_1.isChecked() == True:
            selected1 = "Python"
        if self.btn_2.isChecked() == True:
            selected1 = "Java"
        if self.btn_3.isChecked() == True:
            selected1 = "JavaScript"
        if self.btn_4.isChecked() == True:
            selected2 = "Debit Card"
        if self.btn_5.isChecked() == True:
            selected2 = "PayTM"
        if self.btn_6.isChecked() == True:
            selected2 = "Cash"
        self.label_result.setText("Chosen Book :" + selected1 + " and Chosen Payment Method:" + selected2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_result.setText(_translate("Dialog", "Text"))
        self.label.setText(_translate("Dialog", "Choose Your Book"))
        self.btn_1.setText(_translate("Dialog", "Python"))
        self.btn_2.setText(_translate("Dialog", "Java"))
        self.btn_3.setText(_translate("Dialog", "JavaScript"))
        self.label_2.setText(_translate("Dialog", "Choose Your Payment Method"))
        self.btn_4.setText(_translate("Dialog", "Debit Card"))
        self.btn_5.setText(_translate("Dialog", "PayTM"))
        self.btn_6.setText(_translate("Dialog", "Cash"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
