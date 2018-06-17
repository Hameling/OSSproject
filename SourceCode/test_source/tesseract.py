from PIL import Image
from pytesseract import *
import os
import cv2
import numpy as np


def OCR(imgfile, lang='eng'):
    im = Image.open(imgfile)
    text = image_to_string(im, lang=lang)

    print("OCR Result")
    print(text)

os.chdir('../Tesseract-OCR')


#OCR('C:/Users/user/Documents/OSSproject/SourceCode/practice/2018-05-21.png')
#OCR('../practice/Justice-League_T.jpg')

OCR('../practice/index.png')
