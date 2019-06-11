# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rough.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rough_form import Ui_Form as NameForm
from evaluate_team import Ui_Form as EvaluateForm
from openWindow import Ui_Form as OpenForm
import sqlite3
import sys
import os


playerlist=[]

class Ui_MainWindow(object):
    def __init__(self):
        self.new_form=QtWidgets.QWidget()
        self.evaluate_form=QtWidgets.QWidget()
        self.open_form=QtWidgets.QWidget()
        self.open_screen=OpenForm()
        self.new_screen = NameForm()
        self.evaluate_screen = EvaluateForm()
        self.new_screen.setupUi(self.new_form)
        self.evaluate_screen.setupUi(self.evaluate_form)
        self.open_screen.setupUi(self.open_form)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 791, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.nBatsmen = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nBatsmen.setStyleSheet("color: rgb(52, 101, 164);\n"
"")

        self.nBat=0
        self.nBow=0
        self.nar=0
        self.nwk=0
        self.apts=1000
        self.pused=0


        self.nBatsmen.setObjectName("nBatsmen")
        self.horizontalLayout.addWidget(self.nBatsmen)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.nBowlers = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nBowlers.setStyleSheet("color: rgb(52, 101, 164);")
        self.nBowlers.setObjectName("nBowlers")
        self.horizontalLayout.addWidget(self.nBowlers)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.nAllRounders = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nAllRounders.setStyleSheet("color: rgb(52, 101, 164);")
        self.nAllRounders.setObjectName("nAllRounders")
        self.horizontalLayout.addWidget(self.nAllRounders)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.nWicketKeeper = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nWicketKeeper.setStyleSheet("color: rgb(52, 101, 164);")
        self.nWicketKeeper.setObjectName("nWicketKeeper")
        self.horizontalLayout.addWidget(self.nWicketKeeper)
        self.yourSelection = QtWidgets.QLabel(self.centralwidget)
        self.yourSelection.setGeometry(QtCore.QRect(20, 30, 121, 17))
        self.yourSelection.setAutoFillBackground(False)
        self.yourSelection.setStyleSheet("color: rgb(78, 154, 6);")
        self.yourSelection.setObjectName("yourSelection")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 241, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.availPnts = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.availPnts.setStyleSheet("color: rgb(52, 101, 164);")
        self.availPnts.setObjectName("availPnts")
        self.horizontalLayout_2.addWidget(self.availPnts)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(590, 130, 191, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.usedPnts = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.usedPnts.setStyleSheet("color: rgb(52, 101, 164);")
        self.usedPnts.setObjectName("usedPnts")
        self.horizontalLayout_3.addWidget(self.usedPnts)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 190, 311, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")


       #--------------Radio buttons---------------------------------
        self.bat = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.bat.setEnabled(False)
        self.bat.setObjectName("bat")
        self.horizontalLayout_4.addWidget(self.bat)
        self.bat.clicked.connect(self.listNames)
        self.bow = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.bow.setEnabled(False)
        self.bow.setObjectName("bow")
        self.horizontalLayout_4.addWidget(self.bow)
        self.bow.clicked.connect(self.listNames)
        self.ar = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.ar.setEnabled(False)
        self.ar.setObjectName("ar")
        self.horizontalLayout_4.addWidget(self.ar)
        self.ar.clicked.connect(self.listNames)
        self.wk = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.wk.setEnabled(False)
        self.wk.setObjectName("wk")
        self.horizontalLayout_4.addWidget(self.wk)
        self.wk.clicked.connect(self.listNames)
        #-----------------------------------
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(540, 190, 241, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.teamName = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.teamName.setStyleSheet("color: rgb(52, 101, 164);")
        self.teamName.setObjectName("teamName")
        self.horizontalLayout_5.addWidget(self.teamName)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 250, 781, 301))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.playersList = QtWidgets.QListWidget(self.horizontalLayoutWidget_6)
        self.playersList.setObjectName("playersList")
        self.horizontalLayout_6.addWidget(self.playersList)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.teamList = QtWidgets.QListWidget(self.horizontalLayoutWidget_6)
        self.teamList.setObjectName("teamList")
        self.horizontalLayout_6.addWidget(self.teamList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionQUIT = QtWidgets.QAction(MainWindow)
        self.actionQUIT.setObjectName("actionQUIT")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionQUIT_2 = QtWidgets.QAction(MainWindow)
        self.actionQUIT_2.setObjectName("actionQUIT_2")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addAction(self.actionQUIT_2)
        self.menubar.addAction(self.menuManage_Teams.menuAction())


        #-------- Menu functions added---------------
        self.actionNEW_Team.triggered.connect(self.newTeam)
        self.actionOPEN_Team.triggered.connect(self.openTeam)
        self.actionSAVE_Team.triggered.connect(self.saveTeam)
        self.actionEVALUATE_Team.triggered.connect(self.evaluateTeam)
        self.actionQUIT_2.triggered.connect(MainWindow.close)
        #--------------------------------------------

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Handling Double click
        self.playersList.itemDoubleClicked.connect(self.removeList)
        self.teamList.itemDoubleClicked.connect(self.removeList2)


        self.new_screen.pushButton.clicked.connect(self.namechange)
      
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.nBatsmen.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.nBowlers.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.nAllRounders.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.nWicketKeeper.setText(_translate("MainWindow", "0"))
        self.yourSelection.setText(_translate("MainWindow", "Your Selections"))
        self.label_3.setText(_translate("MainWindow", "Points Available"))
        self.availPnts.setText(_translate("MainWindow", "1000"))
        self.label_8.setText(_translate("MainWindow", "Points Used"))
        self.usedPnts.setText(_translate("MainWindow", "0"))
        self.bat.setText(_translate("MainWindow", "BAT"))
        self.bow.setText(_translate("MainWindow", "BOW"))
        self.ar.setText(_translate("MainWindow", "AR"))
        self.wk.setText(_translate("MainWindow", "WK"))
        self.label.setText(_translate("MainWindow", "Team Name"))
        self.teamName.setText(_translate("MainWindow", "###"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQUIT_2.setText(_translate("MainWindow", "QUIT"))




    def listNames(self):
    	myteam = sqlite3.connect("mycricket.db")
    	cur = myteam.cursor()
    	if self.bat.isChecked():
    		self.playersList.clear()
    		cur.execute("select Player from stats where ctg='BAT';")
    		players = cur.fetchall()
    		i = 0
    		while i<len(players):
    			if players[i][0] not in playerlist:
    				item = QtWidgets.QListWidgetItem(players[i][0])
    				self.playersList.addItem(item)
    			i+=1
    	if self.bow.isChecked():
    		self.playersList.clear()
    		cur.execute("select Player from stats where ctg='BWL';")
    		players=cur.fetchall()
    		i=0
    		while i<len(players):
    			if players[i][0] not in playerlist:
    				item = QtWidgets.QListWidgetItem(players[i][0])
    				self.playersList.addItem(item)
    			i+=1

    	if self.wk.isChecked():
    		self.playersList.clear()
    		cur.execute("select Player from stats where ctg='WK';")
    		players = cur.fetchall()
    		i=0
    		while i<len(players):
    			if players[i][0] not in playerlist:
    				item = QtWidgets.QListWidgetItem(players[i][0])
    				self.playersList.addItem(item)
    			i+=1

    	if self.ar.isChecked():
    		self.playersList.clear()
    		cur.execute("select Player from stats where ctg='AR';")
    		players=cur.fetchall()
    		i=0
    		while i<len(players):
    			if players[i][0] not in playerlist:
    				item = QtWidgets.QListWidgetItem(players[i][0])
    				self.playersList.addItem(item)
    			i+=1
    	myteam.close()


    def removeList(self,item):
    	myteam = sqlite3.connect("mycricket.db")
    	cur = myteam.cursor()
    	if self.bat.isChecked():
    		self.nBat+=1
    		if(self.error()):
    			self.nBat-=1
    			return
    		self.playersList.takeItem(self.playersList.row(item))
    		self.teamList.addItem(item)
    		playerlist.append(item.text())
    		cur.execute("select value from stats where player='"+item.text()+"';")
    		data = cur.fetchone()
    		
    		self.apts-=data[0]
    		self.pused+=data[0]
    		self.availPnts.setText(str(self.apts))
    		self.usedPnts.setText(str(self.pused))

    		self.nBatsmen.setText(str(self.nBat))

    	elif self.bow.isChecked():
    		self.nBow+=1
    		if(self.error()):
    			self.nBow-=1
    			return
    		self.playersList.takeItem(self.playersList.row(item))
    		self.teamList.addItem(item)
    		playerlist.append(item.text())
    		cur.execute("select value from stats where player='"+item.text()+"';")
    		data = cur.fetchone()
    		self.apts-=data[0]
    		self.pused+=data[0]
    		self.availPnts.setText(str(self.apts))
    		self.usedPnts.setText(str(self.pused))
    		self.nBowlers.setText(str(self.nBow))

    	elif self.wk.isChecked():
    		self.nwk+=1
    		if(self.error()):
    			self.nwk-=1
    			return
    		self.playersList.takeItem(self.playersList.row(item))
    		self.teamList.addItem(item)
    		playerlist.append(item.text())
    		cur.execute("select value from stats where player='"+item.text()+"';")
    		data = cur.fetchone()
    		self.apts-=data[0]
    		self.pused+=data[0]
    		self.availPnts.setText(str(self.apts))
    		self.usedPnts.setText(str(self.pused))
    		self.nWicketKeeper.setText(str(self.nwk))

    	elif self.ar.isChecked():
    		self.nar+=1
    		if(self.error()):
    			self.nar-=1
    			return
    		self.playersList.takeItem(self.playersList.row(item))
    		self.teamList.addItem(item)
    		playerlist.append(item.text())
    		cur.execute("select value from stats where player='"+item.text()+"';")
    		data = cur.fetchone()
    		self.apts-=data[0]
    		self.pused+=data[0]
    		self.availPnts.setText(str(self.apts))
    		self.usedPnts.setText(str(self.pused))
    		self.nAllRounders.setText(str(self.nar))







    def removeList2(self,item):
    	conn = sqlite3.connect('mycricket.db')
    	curs = conn.cursor()
    	curs.execute("select value,ctg from stats where player='"+item.text()+"';")
    	data = curs.fetchone()
    	self.teamList.takeItem(self.teamList.row(item))
    	playerlist.remove(item.text())
    	if data[1]=='BAT':
    		self.nBat-=1
    		self.nBatsmen.setText(str(self.nBat))
    	elif data[1]=='BOW':
    		self.nBow-=1
    		self.nBowlers.setText(str(self.nBow))
    	elif data[1]=='AR':
    		self.nar-=1
    		self.nAllRounders.setText(str(self.nar))
    	elif data[1]=='WK':
    		self.nwk-=1
    		self.nWicketKeeper.setText(str(self.wk))

    	self.apts+=data[0]
    	self.pused-=data[0]
    	self.availPnts.setText(str(self.apts))
    	self.usedPnts.setText(str(self.pused))





    def newTeam(self):
    	self.new_form.show()


    	
    def namechange(self):
    	self.teamName.setText(self.new_screen.name)
    	self.bat.setEnabled(True)
    	self.bow.setEnabled(True)
    	self.ar.setEnabled(True)
    	self.wk.setEnabled(True)



    def openTeam(self):
    	self.open_form.show()


    def evaluateTeam(self):
        self.evaluate_form.show()



    def error(self):
        err_box = QtWidgets.QErrorMessage()
        if self.nBat>5:
            err_box.showMessage('Oh no! only 5 batsmen are allowed')
            err_box.exec_()
            return True
        if self.nwk>1:
            err_box.showMessage('Oh no! only 1 Wicket-Keeper is allowed')
            err_box.exec_()
            return True
        if self.nar>2:
            err_box.showMessage('Oh no! only 2 Allrounders are allowed')
            err_box.exec_()
            return True
        if self.nBow>5:
            err_box.showMessage('Oh no! only 5 bowlers are allowed')
            err_box.exec_()
            return True
        if (self.nBat+self.nBow+self.nar+self.nwk)>11:
            err_box.showMessage('Oh no! only 11 players are allowed')
            err_box.exec_()
            return True


    def saveTeam(self):
        team_name=self.teamName.text()
        player_list = []
        for index in range(self.teamList.count()):
            player_list.append(self.teamList.item(index).text())
        conn = sqlite3.connect('mycricket.db')
        cur = conn.cursor()
        for player in player_list:
            cur.execute("select value from stats where player='"+player+"';")
            data = cur.fetchone()
            cur.execute("insert into team(name,players,value) values('"+team_name+"','"+
                player+"',"+str(data[0])+");")
        conn.commit()
        conn.close()
        msg_box=QtWidgets.QMessageBox()
        msg_box.setText("Saved!!!")
        msg_box.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
