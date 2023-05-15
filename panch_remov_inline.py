import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


template = cv2.imread('temp/tem.png',0)
w, h = template.shape[::-1]
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue
    img = cv2.imread(filename,0)
    img2 = img.copy()
    
    

    
    method = eval('cv2.TM_CCOEFF')
        # Apply template Matching
    res = cv2.matchTemplate(img2,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img2,top_left, bottom_right, 248, -1)
    cv2.imwrite(filename,img2)
