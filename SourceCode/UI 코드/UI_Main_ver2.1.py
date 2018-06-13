# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aaaaa.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import string
import cv2
from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import imgproc
import numpy as np



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        global width
        width= 1000
        global height
        height= 800
        btn_x = 80
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #find_btn 버튼 클릭 이벤트 생성
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(width-btn_x, height-790, width/15, height/10))
        self.find_btn.setObjectName("find_btn")
        self.find_btn.clicked.connect(self.find_btnClicked)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("find_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_btn.setIcon(icon)
        self.find_btn.setIconSize(QtCore.QSize(50, 50))
        self.find_btn.setStyleSheet("background-color :#00ff0000")
        
        #run_btn_btn버튼 클릭 이벤트 생성.
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setGeometry(QtCore.QRect(width-btn_x, height-470, width/15, height/10))
        self.run_btn.setObjectName("run_btn")
        self.run_btn.clicked.connect(self.run_btnClicked)
        run_icon = QtGui.QIcon()
        run_icon.addPixmap(QtGui.QPixmap("run_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_btn.setIcon(run_icon)
        self.run_btn.setIconSize(QtCore.QSize(50, 50))
        self.run_btn.setStyleSheet("background-color :#00ff0000")
        self.run_btn.hide()
        
        #리셋버튼 생성 및 이벤트
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(width-btn_x, height-650, width/15, height/10))
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.clicked.connect(self.reset_btnClicked)
        reset_icon = QtGui.QIcon()
        reset_icon.addPixmap(QtGui.QPixmap("reset_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_btn.setIcon(reset_icon)
        self.reset_btn.setIconSize(QtCore.QSize(50, 50))
        self.reset_btn.setStyleSheet("background-color :#00ff0000")
        

        #quit_btn
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(width-btn_x, height-150, 63, 51))
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.clicked.connect(self.quit_btnClicked)
        #save
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(width-btn_x, height-250, 63, 51))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.saveClicked)
        self.save_btn.hide()
        
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
        #self.label.hide()
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

        #가로가 길 경우의 이미지 라벨올릴 레이아웃
        self.gridLayoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget3.setGeometry(QtCore.QRect(width-990, height-790, width-100, height-150))
        self.gridLayoutWidget3.setObjectName("gridLayoutWidget1")
        self.gridLayout3 = QtWidgets.QGridLayout(self.gridLayoutWidget3)
        self.gridLayout3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout3.setObjectName("gridLayout1")
        
        #가로가 길 경우의 이미지 라벨
        self.label2 = QtWidgets.QLabel(self.gridLayoutWidget3)#라벨 생성
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("black.png"))#시작 이미지
        self.label2.hide()

        #가로가 길 경우의 텍스트 브라우저 올릴 레이아웃
        self.gridLayoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget4.setGeometry(QtCore.QRect(width-990, height-200, width-100, height-700))
        self.gridLayoutWidget4.setObjectName("gridLayoutWidget1")
        self.gridLayout4 = QtWidgets.QGridLayout(self.gridLayoutWidget4)
        self.gridLayout4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout4.setObjectName("gridLayout1")
        
        #가로가 길 경우의 텍스트 브라우저
        self.textBrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget4)
        self.textBrowser1.setObjectName("textBrowser")
        self.gridLayout4.addWidget(self.textBrowser1, 0, 0, 0,0)
        self.textBrowser1.hide()
       
       

        
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)#그리드 레이아웃 내의위치
        self.gridLayout1.addWidget(self.label1, 0, 0, 1, 1)#그리드 레이아웃 내의위치
        self.gridLayout3.addWidget(self.label2, 0, 0, 1, 1)#그리드 레이아웃 내의위치
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
        #self.actionExit.triggered.cinnect(qApp.quit_btn)
        #self.menuMenu.addAction(self.actionLouge)
        self.menuMenu.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.actionExitClicked)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.find_btn.setText(_translate("MainWindow", ""))
        self.run_btn.setText(_translate("MainWindow", ""))
        self.reset_btn.setText(_translate("MainWindow", ""))
        self.quit_btn.setText(_translate("MainWindow", "quit_btn"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        #self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        #self.actionLouge.setText(_translate("MainWindow", "louge"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))

    def find_btnClicked(self):
        file_path =  QFileDialog.getOpenFileName(None,'파일 탐색','c\\',"image files (*.png *.jpg)")
        print(file_path)
        if(file_path==('', '')):
             self.label.setText("선택된 이미지가 없습니다.")  
             return
        file_path_str = str(file_path)#경로 string으로 변환
        
        global file_name
        #print(file_path_str)#경로 확인 현상태 경로+파일 타입
        path_adress = file_path_str.find(',')#경로길이 계산. ','을 기점으로 앞부분이 경로 뒷부분이 파일 유형.
        print(path_adress-1)
        print(file_path_str[1:path_adress])#(제외 처음부터 ","앞까지
        sel_img= file_path_str[2:path_adress-1]
        print(file_path_str[1:path_adress])
        #sel_img1= sel_img.replace('\\','\\\\')#경로에 \ 하나가 더 추가되야 되서 저렇게 씀.
        print(sel_img,"\n\n\n")#경로 재확인
        #im = Image.open(sel_img)#이미지 받음
        
        og_img, re_img, cimg_root, cimg_result = imgproc.ImgProc(sel_img)
        
        #이전 버전
        #og_img = cv2.resize(og_img, None, fx  = 0.9, fy = 0.9, interpolation=cv2.INTER_AREA)
        #re_img = cv2.resize(re_img, None, fx = 0.9, fy = 0.9, interpolation=cv2.INTER_AREA)
        
        #최신 버전
        #og_img = cv2.resize(og_img, (int(width*0.9), int(height*0.9)),interpolation=cv2.INTER_AREA)
        #re_img = cv2.resize(re_img, (int(width*0.7), int(height*0.7)), interpolation=cv2.INTER_AREA)

        #BGR->RGB 변환 
        b, g, r = cv2.split(og_img)
        og_img = cv2.merge([r,g,b])

        b, g, r = cv2.split(re_img)
        re_img = cv2.merge([r,g,b])
        
        og_height, og_width, channel = og_img.shape
       
        print(str(og_width)+", "+str(og_height))
        

        #결과 화면 이미지 크기 조절은 0.7을 수정해주면된다
        if og_width > width or og_height > height:
            print("길이가 넘습니다")
            if (og_width - width) > (og_height - height):
                ratio = width / og_width
                og_img = cv2.resize(og_img, (int(width * 0.9), int(og_height * 0.9 * ratio )),interpolation=cv2.INTER_AREA)
                re_img = cv2.resize(re_img, (int(width * 0.7), int(og_height * 0.7 * ratio )),interpolation=cv2.INTER_AREA)
            else:
                ratio = height / og_height
                og_img = cv2.resize(og_img, (int(og_width * 0.9 * ratio), int(height * 0.9)),interpolation=cv2.INTER_AREA)
                re_img = cv2.resize(re_img, (int(og_width * 0.7 * ratio), int(height * 0.7)),interpolation=cv2.INTER_AREA)
        else:
            og_img = cv2.resize(og_img, (int(og_width*0.9), int(og_height*0.9)),interpolation=cv2.INTER_AREA)
            re_img = cv2.resize(re_img, (int(og_width*0.7), int(og_height*0.7)), interpolation=cv2.INTER_AREA)

        

        #원본 이미지
        og_height, og_width, channel = og_img.shape
        og_qimg = QtGui.QImage(og_img.data, og_width, og_height, og_width*3, QtGui.QImage.Format_RGB888 )

        #출력할 이미지
        re_height, re_width, channel = re_img.shape
        qimg = QtGui.QImage(re_img.data, re_width, re_height, re_width*3, QtGui.QImage.Format_RGB888 )
       

        self.label.setPixmap(QtGui.QPixmap(og_qimg))
        
        global control
        
        ##만들어줘야되는 부분
        if og_width > og_height:
            #    #가로가 더 길때
            control = "w"
            self.label2.setPixmap(QtGui.QPixmap(qimg))
            
        
        else :
            control = "h"
            self.label1.setPixmap(QtGui.QPixmap(qimg))
        #    #세로가 더 길때
        self.run_btn.show()#run_btn 보이기
        self.label1.hide()
        self.label2.hide()
        self.textBrowser.hide()
        self.textBrowser1.hide()
        self.label.show()

        

               

    def actionExitClicked(self):#종료
        quit()
    
    def run_btnClicked(self):
        #dlg = ResultDialog()
        #dlg.exec_()
        self.label.hide()#화면 전환
        self.label1.hide()
        self.label2.hide()
        self.textBrowser.hide()
        self.textBrowser1.hide()
        self.run_btn.hide()
        self.save_btn.show()
        self.run_btn.hide()
        if control == "h" :
            self.label1.show()#화면 전환
            self.textBrowser.show()
            i=0
            while i!=10:
                self.textBrowser.append("\tHello Pyqt5\b")
                count = str(i)
                self.textBrowser.append(count)
                i=i+1
        else :
            self.label2.show()#화면 전환
            self.textBrowser1.show()
            i=0
            while i!=10:
                self.textBrowser1.append("\tHello Pyqt5\b")
                count = str(i)
                self.textBrowser1.append(count)
                i=i+1

        
        
        #append 실험용 코드
        
        

    def reset_btnClicked(self):#초기 화면 상태로 회귀
        self.run_btn.hide()
        self.label.setPixmap(QtGui.QPixmap("background.png"))#시작 텍스트
        self.label1.hide()
        self.label2.hide()
        self.label.show()
        self.save_btn.hide()
        self.textBrowser.clear()
        self.textBrowser.hide()
        self.textBrowser1.clear()
        self.textBrowser1.hide()

    def quit_btnClicked(self):#종료
        MainWindow.close()

    def saveClicked(self):
        file_dir = QFileDialog.getExistingDirectory(None,'파일 경로','c\\')
        print(file_dir)
        Newline = '/'
        file_dir = file_dir+Newline
        print(file_dir)
        

        #dlg.find_btnClicked(self,sel_img)
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

