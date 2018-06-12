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
        global width
        width= 1000
        global height
        height= 800
        btn_x = 80
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width,height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #find 버튼 클릭 이벤트 생성
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(width-btn_x, height-790, width/15, height/10))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        #Run버튼 클릭 이벤트 생성.
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(width-btn_x, height-470, width/15, height/10))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.runClicked)
        self.pushButton_2.hide()
        #대기 버튼 생성
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(width-btn_x, height-470, width/15, height/10))
        #리셋버튼 생성 및 이벤트
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(width-btn_x, height-650, width/15, height/10))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.resetClicked)
        #quit
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(width-btn_x, height-150, 63, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.quitClicked)
        #save
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(width-btn_x, height-250, 63, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.saveClicked)
        self.pushButton_6.hide()
        
        #label 올릴 거
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(width-990, height-790, width-100, height-100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #아래부터 이미지 보일 라벨 생성
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)#라벨 생성
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.png"))#시작 텍스트
        self.label.setObjectName("label")#라벨 이름
        #label1올릴거
        self.gridLayoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget1.setGeometry(QtCore.QRect(width-990, height-790, width-500, height-100))
        self.gridLayoutWidget1.setObjectName("gridLayoutWidget1")
        self.gridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget1)
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout1.setObjectName("gridLayout1")
         #아래부터 이벤트 후 이미지 생성.
        self.label1 = QtWidgets.QLabel(self.gridLayoutWidget1)#라벨 생성
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("556.jpg"))#시작 텍스트
        self.label1.hide()
        #텍스트 브라우저 올릴 곳.
        self.gridLayoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget2.setGeometry(QtCore.QRect(width-490, height-790, width-600, height-100))
        self.gridLayoutWidget2.setObjectName("gridLayoutWidget2")
        self.gridLayout2 = QtWidgets.QGridLayout(self.gridLayoutWidget2)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setObjectName("gridLayout2")
        #텍스트 에리어 삽입
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout2.addWidget(self.textBrowser, 0, 0, 0,0)
        self.textBrowser.hide()
        
       
       

        
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)#그리드 레이아웃 내의위치
        self.gridLayout1.addWidget(self.label1, 0, 0, 1, 1)#그리드 레이아웃 내의위치
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
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
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
        sel_img= file_path_str[2:path_adress-1]
        print(file_path_str[1:path_adress])
        #sel_img1= sel_img.replace('\\','\\\\')#경로에 \ 하나가 더 추가되야 되서 저렇게 씀.
        print(sel_img,"\n\n\n")#경로 재확인
        im = Image.open(sel_img)#이미지 받음
        rgb_im = im.convert('RGB')#png파일 >>jpg파일
        rgb_im1= rgb_im
        rgb_im=rgb_im.resize((width-100,height-100))
        rgb_im.save('show.jpg')#배경 이미지 하나 넣을 것.
        #im.show()#확인용 열기.
        self.label.setPixmap(QtGui.QPixmap('show.jpg'))
        rgb_im1=rgb_im1.resize((width-500,height-100))
        rgb_im1.save('show1.jpg')#배경 이미지 하나 넣을 것.
        self.label1.setPixmap(QtGui.QPixmap('show1.jpg'))
        self.pushButton_3.hide()#waiting 숨기기
        self.pushButton_2.show()#run 보이기
        

    def actionExitClicked(self):#종료
        quit()
    
    def runClicked(self):
        #dlg = ResultDialog()
        #dlg.exec_()
        self.label.hide()#화면 전환
        self.label1.show()#화면 전환
        self.textBrowser.show()
        self.pushButton_2.hide()
        self.pushButton_6.show()
        #append 실험용 코드
        i=0
        while i!=10:
            self.textBrowser.append("\tHello Pyqt5\b")
            count = str(i)
            self.textBrowser.append(count)
            i=i+1
        

    def resetClicked(self):#초기 화면 상태로 회귀
        self.pushButton_2.hide()
        self.pushButton_3.show()
        self.label.setPixmap(QtGui.QPixmap("background.png"))#시작 텍스트
        self.label1.hide()
        self.label.show()
        self.pushButton_6.hide()
        self.textBrowser.clear()
        self.textBrowser.hide()

    def quitClicked(self):#종료
        MainWindow.close()

    def saveClicked(self):
        file_dir = QFileDialog.getExistingDirectory(None,'파일 경로','c\\')
        print(file_dir)
        Newline = '/'
        file_dir = file_dir+Newline
        print(file_dir)
        
                

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

