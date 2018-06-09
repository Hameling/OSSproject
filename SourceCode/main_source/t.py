import cv2
import numpy as np
import random
import os
from matplotlib import pyplot as plt

def BoxWarp(img, box):

    rect = np.zeros((4,2),dtype = 'float32')
    
    s = box.sum(axis = 1)
    rect[0] = box[np.argmin(s)]
    rect[2] = box[np.argmax(s)]

    diff = np.diff(box, axis = 1)
    rect[1] = box[np.argmin(diff)]
    rect[3] = box[np.argmax(diff)]

    print(rect)
    (tl, tr, br, bl) = rect
    #(bl,tl,tr,br) = box

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], np.float32)


    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))

    return warped


file_name = 'practice/home-video-message.png'

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

#Image Kernel 정의
mp_kernel = np.ones((2,2),np.uint8)
sh_kernel = np.array([[-1,-1,-1], [-1,10,-1], [-1,-1,-1]])
br_kenrnel = np.array([[1/16, 1/8, 1/16],[1/8,1/4,1/8],[1/16, 1/8, 1/16]])


cv2.imshow("gray_image",imgray)
#imgray = cv2.equalizeHist(imgray)
#cv2.imshow("His_image",imgray)

imgray = cv2.filter2D(imgray, -1, sh_kernel)
#imgray = cv2.filter2D(imgray,-1,br_kenrnel)
cv2.imshow("Sharp_image",imgray)

mp = cv2.morphologyEx(imgray, cv2.MORPH_GRADIENT,mp_kernel)
tmp_img = np.copy(mp)
mp = cv2.morphologyEx(mp, cv2.MORPH_CLOSE,mp_kernel)

thresh = cv2.adaptiveThreshold(mp,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,7,2)
thresh = ~thresh



image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



for i in range(len(contours)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)
    if cv2.contourArea(contours[i]) > 500:
        cnt = contours[i]
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        print(box)
        #img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2) 
        img = cv2.drawContours(img, [box], -1,(b,g,r), 2) 

        wp_img = BoxWarp(tmp_img,box)
       
        contoured_img = 'Contour_img/' + file_name + str(i)
        cv2.imwrite(contoured_img+'.jpg',wp_img)



cv2.imshow('thresh',thresh)
cv2.imshow('temp image',tmp_img)
cv2.imshow('image',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()