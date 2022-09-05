# QComboBox using QT Designer Example
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # Connecting signal to slot
        self.comboBox.currentIndexChanged.connect(self.combo_changed)

        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Kokila")
        font.setPointSize(18)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def combo_changed(self):
        item = self.comboBox.currentText()
        self.result.setText("You have selected : **" + item + "** programming language.")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select your Favourite Language :"))
        self.comboBox.setItemText(0, _translate("Form", "Python"))
        self.comboBox.setItemText(1, _translate("Form", "Java"))
        self.comboBox.setItemText(2, _translate("Form", "C++"))
        self.comboBox.setItemText(3, _translate("Form", "JavaScript"))
        self.comboBox.setItemText(4, _translate("Form", "C#"))
        self.comboBox.setItemText(5, _translate("Form", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
