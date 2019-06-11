

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Form(object):
    def __init__(self):
        self.name=''
        self.form=None
    def setupUi(self, Form):
        self.form=Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 80, 131, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 231, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 170, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.name=''
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.exit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter Team name"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))

    def confirm(self):
        self.name = self.lineEdit.text()
        self.lineEdit.clear()
        self.form.close()

    def exit(self):
        self.name=''
        self.lineEdit.clear()
        self.form.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    print(ui.name)
    app.exec_()
    
    sys.exit()
