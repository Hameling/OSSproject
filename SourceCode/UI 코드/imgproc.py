import cv2
import numpy as np
import random
import os
from boxwarp import BoxWarp




def ImgProc(file_name):

    if file_name.find('png') != -1 :
        img = cv2.imread(file_name,cv2.IMREAD_COLOR)
        imgray = cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)
        flag = 1
    elif file_name.find('jpg') != -1 :
        img = cv2.imread(file_name)
        imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        flag = 2
    else: exit()

    file_name = file_name.split('/')
    file_name = file_name[-1]

    og_img = np.copy(img)
    tmp_img = np.copy(imgray)
    
    #height, width 계산
    height = np.size(img, 0)
    width = np.size(img, 1)
    
    print(height, width)
    
    #Image Kernel 정의
    mp_kernel = np.ones((2,2),np.uint8)
    
    
    #cv2.imshow("gray_image",imgray)
    
    thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,7,2)
    thresh = ~thresh
    
    
    mp = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,mp_kernel)
    mp = cv2.morphologyEx(mp, cv2.MORPH_CLOSE,mp_kernel)
    
    tmp_img= cv2.morphologyEx(tmp_img, cv2.MORPH_GRADIENT,mp_kernel)
    
    #cv2.imshow("mp",mp)
    
    
    minLineLength = 100
    maxLineGap = 5
    
    lines = cv2.HoughLinesP(mp,1,np.pi/360,100,minLineLength,maxLineGap)
    
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            #print(x1,y1,x2,y2)
            if abs(y2-y1) > (height/20):
                cv2.line(mp,(x1,y1),(x2,y2),(0,0,255),10)
    
    
    image, contours, hierarchy = cv2.findContours(mp, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    
    cimg_root = []
    cimg_result = []
    for i in range(len(contours)):
        #각 Contour Line을 구분하기 위해서 Color Random생성
        b = random.randrange(1,255)
        g = random.randrange(1,255)
        r = random.randrange(1,255)
    
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        wp_img,dst = BoxWarp(tmp_img,box)
        if dst[1][0] > int(width/30) or dst[3][1] > int(height/30):
        #if dst[1][0] > 30 and dst[3][1] > 10:
        #if w > 10 or h > 10:
            #rect = cv2.minAreaRect(cnt)
            #box = cv2.boxPoints(rect)
            #box = np.int0(box)
            #print(box)
            img = cv2.drawContours(img, [box], -1,(b,g,r), 2) 
            #img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #wp_img = BoxWarp(tmp_img,box)
            cimg_result.append(wp_img)
            contoured_img = 'Contour_img/' + file_name + str(i)
            cimg_root.append(contoured_img)
            #print(contoured_img)
            cv2.imwrite(contoured_img+'.jpg',wp_img)
 

    #cv2.imshow('thresh',thresh)
    #cv2.imshow('temp image',tmp_img)
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return og_img, img, cimg_root, cimg_result