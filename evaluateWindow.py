# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_team.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
class Ui_Form(object):
    def __init__(self):
        self.msg_box = QtWidgets.QMessageBox()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 514)
        Form.setMinimumSize(QtCore.QSize(632, 514))
        Form.setMaximumSize(QtCore.QSize(632, 514))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 211, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teamSelect = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.teamSelect.setObjectName("teamSelect")
        self.horizontalLayout.addWidget(self.teamSelect)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 150, 571, 291))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.evaluate_team_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.evaluate_team_list.setStyleSheet("color: rgb(173, 127, 168);")
        self.evaluate_team_list.setObjectName("evaluate_team_list")
        self.horizontalLayout_2.addWidget(self.evaluate_team_list)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scorelist = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.scorelist.setStyleSheet("color: rgb(52, 101, 164);")
        self.scorelist.setObjectName("scorelist")
        self.horizontalLayout_2.addWidget(self.scorelist)
        self.evaluate = QtWidgets.QPushButton(Form)
        self.evaluate.setGeometry(QtCore.QRect(240, 470, 121, 25))
        self.evaluate.setObjectName("evaluate")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(390, 70, 201, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("Match_1")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 341, 17))
        self.label.setStyleSheet("color: rgb(78, 154, 6);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(390, 120, 51, 17))
        self.label_3.setObjectName("label_3")
        self.teamScore = QtWidgets.QLabel(Form)
        self.teamScore.setGeometry(QtCore.QRect(440, 120, 67, 17))
        self.teamScore.setStyleSheet("color: rgb(114, 159, 207);")
        self.teamScore.setObjectName("teamScore")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        conn = sqlite3.connect("mycricket.db")
        cur = conn.cursor()
        cur.execute("select distinct name from team")
        listeams=cur.fetchall()
        self.teamSelect.addItem("Select Team")
        for index in range(len(listeams)):
            self.teamSelect.addItem(str(listeams[index][0]))
        self.teamSelect.activated.connect(self.teamShow)
        self.teamSelect.currentTextChanged.connect(self.teamShow)
        self.comboBox_2.currentTextChanged.connect(self.teamShow)

        self.evaluate.clicked.connect(self.calculate)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.evaluate.setText(_translate("Form", "calculate Score"))
        self.comboBox_2.setItemText(0,_translate("Form","Select Match"))
        self.comboBox_2.setItemText(1, _translate("Form", "Match_1"))
        self.comboBox_2.setItemText(2, _translate("Form", "Match_2"))
        self.comboBox_2.setItemText(3, _translate("Form", "Match_3"))
        self.comboBox_2.setItemText(4, _translate("Form", "Match_4"))
        self.label.setText(_translate("Form", "Evaluate the performance of your fantasy team"))
        self.label_2.setText(_translate("Form", "Players"))
        self.label_3.setText(_translate("Form", "scores"))
        self.teamScore.setText(_translate("Form", "###"))


    def teamShow(self):
        self.evaluate_team_list.clear()
        self.scorelist.clear()
        team = self.teamSelect.currentText()
        conn = sqlite3.connect("mycricket.db")
        cur = conn.cursor()
        cur.execute("select players from team where name='"+team+"';")
        players=cur.fetchall()
        for items in players:
            self.evaluate_team_list.addItem(items[0])
        #calculating scores
        scores=[0 for _ in range(len(players))]
        for index in range(len(players)):
            cur.execute("select * from match where player='"+players[index][0]+"';")
            data=cur.fetchone()
            
            scores[index]+=(int(data[1])//2 + int(data[3])+int(data[4])*2 +int(data[8])*10
                +int(data[9])*10+int(data[10])*10)
            if self.comboBox_2.currentText()=='Match_1':
                random.seed(index+1)
                scores[index]+=random.randint(1,100)
            elif self.comboBox_2.currentText()=='Match_2':
                random.seed(index+2)
                scores[index]+=random.randint(1,100)
            elif self.comboBox_2.currentText()=='Match_3':
                random.seed(index+3)
                scores[index]+=random.randint(1,100)
            elif self.comboBox_2.currentText()=='Match_4':
                random.seed(index+4)
                scores[index]+=random.randint(1,100)
            else:
                scores[index]=0
        for score in scores:
            self.scorelist.addItem(str(score))



    def calculate(self):
        score=0
        for index in range(self.scorelist.count()):
            score+=int(self.scorelist.item(index).text())
        self.teamScore.setText(str(score))
        
        self.msg_box.setText("Score: "+self.teamScore.text())
        self.ok=self.msg_box.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
