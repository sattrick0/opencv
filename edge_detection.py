#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:18:43 2018

@author: root1
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)                                       #load the webcam -- default (0)

while True:
    _, frame = cap.read()                                       #read the frames 
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)                #read the frames in Laplacian mode
   # sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)        #read the frames in Sobel mode
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)        #read the frames in Sobel mode
    edges = cv2.Canny(frame, 100, 200)                          #draw the shape matches edges
        
    cv2.imshow("originan",frame)                                #show image in original
    cv2.imshow("laplacian", laplacian)                          #show image in laplacian
    cv2.imshow("edges", edges)                                  #show image in Canny
    cv2.imshow("sobely", sobely)                                #show images in sobely
        
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()