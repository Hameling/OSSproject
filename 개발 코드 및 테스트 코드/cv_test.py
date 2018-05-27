import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread('img.png', cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((2,2),np.uint8)
##dilated = cv2.dilate(gray_img,kernel,iterations=1)

gradient = cv2.morphologyEx(gray_img, cv2.MORPH_GRADIENT, kernel);

##thresh = cv2.threshold(gradient,127,255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                            cv2.THRESH_BINARY,2,2)


##print(img.shape)

cv2.imshow('image', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
