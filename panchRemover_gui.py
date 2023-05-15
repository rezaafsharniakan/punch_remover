
from tkinter import* 
from tkinter import filedialog as fd
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import glob2
from PIL import Image
import cv2_ext

dir1=''

def croper(dir1):

 

    dir=glob2.glob(dir1+'/*.jpg', recursive=True)
    c=10
    for i in dir:
        
        
        img = cv2_ext.imread(i)
        imt=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        x,y=imt.shape
        p=x-c
        t=y-c

        img2=img[c:p,c:t]
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2_ext.imwrite(i,img2)
        print('crop ok')



def ponchR( dir1):
    
    dir=glob2.glob(dir1+'/*.jpg', recursive=True)

    template = cv2.imread('temp/tem.png',0)
    w, h = template.shape[::-1]  
    for i in dir:
        # img = cv2_ext.imread(i)
        img = cv2.imread(i)
        if img is None: 
            print('cannot imge read')   
   
        else :     
            
            res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
            threshold = 0.65
            loc = np.where( res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 248, -1)
            
            # cv2_ext.imwrite(i,img)
            cv2.imwrite(i,img)
            print('complit')
           
    


def selectDir():
    global dir1
    dir1 =  fd.askdirectory(title = "Select the Folder")
    print(dir1)
    
    button2.pack()
    button3.pack()
    

win=Tk()
win.title('punchremover')
win.geometry('250x200')
button=Button(win,text='browes',command=selectDir)
button.pack()
button2=Button(win,text='punchremover',command=(lambda: ponchR(dir1)))
button3=Button(win,text='croper10px',command=(lambda: croper(dir1)))
    

#dir1 =  fd.askdirectory(title = "Select the Folder")







mainloop()



