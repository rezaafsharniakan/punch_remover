import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


template = cv2.imread('temp/tem.jpg',0)
w, h = template.shape[::-1]
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue
    img_rgb = cv2.imread(filename,0)
    #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.65
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), 248, -1)
   
    cv2.imwrite(filename,img_rgb)
