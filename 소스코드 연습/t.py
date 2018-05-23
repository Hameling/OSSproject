import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('img.png')
##img = cv2.imread('image012.png',cv2.IMREAD_GRAYSCALE)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((2,2),np.uint8)
mp = cv2.morphologyEx(imgray, cv2.MORPH_GRADIENT,kernel)

##ret,thresh = cv2.threshold(mp,125,255,0)
thresh = cv2.adaptiveThreshold(mp,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,5,2)
thresh = ~thresh
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt = contours[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)


cv2.imshow('thresh',thresh)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#titles = ['Result']
#images = [img]

#for i in range(1):
#    plt.subplot(1,1,i+1), plt.title(titles[i]), plt.imshow(images[i])
#    plt.xticks([]), plt.yticks([])

#plt.show()


#img = cv2.imread('img.png',0)
###img = cv2.medianBlur(img,5)

#kernel = np.ones((2,2),np.uint8)
###dilated = cv2.dilate(gray_img,kernel,iterations=1)

#img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel);


#ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)

#th3 = ~th3
#rimg, countour, hierachy = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#rimg = cv2.drawContours(img, countour, -1, (0,0,0),0)

###kernel = np.ones((5,5),np.uint8)
###th2 = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel);




#titles = ['Original Image', 'Global Thresholding (v = 127)',
#            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
#images = [img, th1, th2, th3]

#for i in range(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

###cv2.imwrite('result.png',rimg)
