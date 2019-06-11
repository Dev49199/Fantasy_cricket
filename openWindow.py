

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 502)
        Form.setMinimumSize(QtCore.QSize(506, 502))
        Form.setMaximumSize(QtCore.QSize(506, 502))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.label.setObjectName("label")
        self.teamCombo = QtWidgets.QComboBox(Form)
        self.teamCombo.setGeometry(QtCore.QRect(150, 50, 151, 25))
        self.teamCombo.setMinimumSize(QtCore.QSize(151, 25))
        self.teamCombo.setMaximumSize(QtCore.QSize(151, 25))
        self.teamCombo.setObjectName("teamCombo")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 100, 271, 331))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 460, 131, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 460, 101, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        conn_1 = sqlite3.connect("mycricket.db")
        cur_1 = conn_1.cursor()
        cur_1.execute("select distinct name from team")
        data = cur_1.fetchall()
        for i in data:
            self.teamCombo.addItem(i[0])
        conn_1.close()
        self.pushButton_2.clicked.connect(self.listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.showTeams)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Team Name"))
        self.pushButton.setText(_translate("Form", "show"))
        self.pushButton_2.setText(_translate("Form", "reset"))

    def showTeams(self):
        self.listWidget.clear()
        conn_2 = sqlite3.connect('mycricket.db')
        x = self.teamCombo.currentText()
        cur_2 = conn_2.cursor()
        cur_2.execute("select players from team where name='"+x+"';")
        y = cur_2.fetchall()
        
        for team in y:
            self.listWidget.addItem(team[0])
        conn_2.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
