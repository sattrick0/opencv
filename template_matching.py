#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:28:36 2018

@author: root1
"""

import cv2
import numpy as np

img_bgr = cv2.imread("main.jpg")                                          #read the image file
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)                        #convert the image into grayscale

template = cv2.imread("template.jpg", 0)                                         #read the template image
w, h = template.shape[::-1]                                                 #reshape the image in reverse order

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)           #matche the template
threshold = 0.8                                                 
loc = np.where(res >= threshold)                                            #load only values which are >= thershold value        


for pt in zip(*loc[::-1]):                                          
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)          #draw rectangle around matched
    
cv2.imshow("detected", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
