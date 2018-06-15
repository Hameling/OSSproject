# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aaaaa.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import string
from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image, ImageTk


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 93, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        #버튼 클릭 이벤트 생성.
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 50, 542, 962))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("3.jpg"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 500, 100, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        #self.actionExit.triggered.cinnect(qApp.quit)
        self.actionLouge = QtWidgets.QAction(MainWindow)
        self.actionLouge.setObjectName("actionLouge")
        self.menuMenu.addAction(self.actionLouge)
        self.menuMenu.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.actionExitClicked)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Find"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        self.actionLouge.setText(_translate("MainWindow", "louge"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))


    def pushButtonClicked(self):
        file_path =  QFileDialog.getOpenFileName(None,'파일 탐색','c\\',"image files (*.png *.jpg)")
        file_path_str = str(file_path)#경로 string으로 변환
        #print(file_path_str)#경로 확인 현상태 경로+파일 타입
        path_adress = file_path_str.find(',')#경로길이 계산. ','을 기점으로 앞부분이 경로 뒷부분이 파일 유형.
        print(path_adress-1)
        print(file_path_str[1:path_adress])#(제외 처음부터 ","앞까지
        sel_img = file_path_str[2:path_adress-1]
        print(file_path_str[1:path_adress])
        #sel_img1= sel_img.replace('\\','\\\\')#경로에 \ 하나가 더 추가되야 되서 저렇게 씀.
        print(sel_img,"\n\n\n")#경로 재확인
        im = Image.open(sel_img)#이미지 받음
        #im.show()#확인용 열기.
        self.label.setPixmap(QtGui.QPixmap(sel_img))

    def actionExitClicked(self):
        quit()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

