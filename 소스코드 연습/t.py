import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img2.jpg',0)
##img = cv2.medianBlur(img,5)

kernel = np.ones((2,2),np.uint8)
##dilated = cv2.dilate(gray_img,kernel,iterations=1)

img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel);


ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

th2 = ~th2
th3 = ~th3
rimg, countour, hierachy = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rimg = cv2.drawContours(img, countour, -1, (0,255,0),3)

##kernel = np.ones((5,5),np.uint8)
##th2 = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel);

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
