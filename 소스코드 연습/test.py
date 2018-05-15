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

os.chdir('C:\Program Files (x86)\Tesseract-OCR')


OCR('result.png')
