#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:02:37 2018
"""

import cv2
import numpy as np

img = cv2.imread("qwerty.png")                      #read image file
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #convert image to grayscale
gray = np.float32(gray)                             #convert array into float

cornors = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)      #array, edges, threshold, gradient
cornors = np.int0(cornors)

for i in cornors:
    print(i)
    x, y = i.ravel()                                #split array 
    cv2.circle(img, (x,y), 3, 25, -1)               #display the edges in circle shape
    
cv2.imshow("cornors", img)                          #display the image
cv2.waitKey(0)                                      #press key 0 or esc to exit
cv2.destroyAllWindows()                             #destroy the activity