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
#import result_s

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #find 버튼 클릭 이벤트 생성
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 50, 63, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        #Run버튼 클릭 이벤트 생성.
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 427, 63, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.runClicked)
        self.pushButton_2.hide()
        #대기 버튼 생성
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 427, 63, 131))
        #리셋버튼 생성 및 이벤트
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 101, 63, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.resetClicked)
        #quit
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 558, 63, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.quitClicked)
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 50, 500, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout1")

        self.gridLayoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget1.setGeometry(QtCore.QRect(100, 50, 500, 500))
        self.gridLayoutWidget1.setObjectName("gridLayoutWidget")
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.setObjectName("gridLayout")
        #아래부터 이미지 보일 라벨 생성
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)#라벨 생성
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("nomal.png"))#시작 텍스트
        self.label.setObjectName("label")#라벨 이름
        #아래부터 이벤트 후 이미지 생성.
        self.label1 = QtWidgets.QLabel(self.gridLayoutWidget1)#라벨 생성
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("556.jpg"))#시작 텍스트
        self.label1.hide()

        
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)#그리드 레이아웃 내의위치
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
        self.pushButton_2.setText(_translate("MainWindow", "Run"))
        self.pushButton_3.setText(_translate("MainWindow", "waiting"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.pushButton_5.setText(_translate("MainWindow", "Quit"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        self.actionLouge.setText(_translate("MainWindow", "louge"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))

    def pushButtonClicked(self):
        file_path =  QFileDialog.getOpenFileName(None,'파일 탐색','c\\',"image files (*.png *.jpg)")
        print(file_path)
        if(file_path==('', '')):
             self.label.setText("선택된 이미지가 없습니다.")  
             return
        file_path_str = str(file_path)#경로 string으로 변환
        #print(file_path_str)#경로 확인 현상태 경로+파일 타입
        path_adress = file_path_str.find(',')#경로길이 계산. ','을 기점으로 앞부분이 경로 뒷부분이 파일 유형.
        print(path_adress-1)
        print(file_path_str[1:path_adress])#(제외 처음부터 ","앞까지
        global sel_img
        sel_img= file_path_str[2:path_adress-1]
        print(file_path_str[1:path_adress])
        #sel_img1= sel_img.replace('\\','\\\\')#경로에 \ 하나가 더 추가되야 되서 저렇게 씀.
        print(sel_img,"\n\n\n")#경로 재확인
        im = Image.open(sel_img)#이미지 받음
        global rgb_im
        rgb_im = im.convert('RGB')#png파일 >>jpg파일
        rgb_im=rgb_im.resize((500,700))
        rgb_im.save('show.jpg')#배경 이미지 하나 넣을 것.
        #im.show()#확인용 열기.
        self.label.setPixmap(QtGui.QPixmap('show.jpg'))
        self.pushButton_3.hide()
        self.pushButton_2.show()
        

    def actionExitClicked(self):
        quit()
    
    def runClicked(self):
        #dlg = ResultDialog()
        #dlg.exec_()
        print(sel_img)
        self.label.hide()
        self.label1.show()

    def resetClicked(self):
        self.pushButton_2.hide()
        self.pushButton_3.show()
        self.label.setPixmap(QtGui.QPixmap("nomal.png"))#시작 텍스트
        self.label1.hide()
        self.label.show()

    def quitClicked(self):
        MainWindow.close()

        #dlg.pushButtonClicked(self,sel_img)
        #id = dlg.id
        #password = dlg.password
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
     
    MainWindow.show()
    sys.exit(app.exec_())

