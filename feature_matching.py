#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:19:59 2018

@author: root1
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("watch.jpg", 1)                                           #read the search image
img2 = cv2.imread("aa.jpeg", 1)                                             #read the match image            

orb = cv2.ORB_create()                                                      #Oriented FAST and Rotated BRIEF

kp1, des1 = orb.detectAndCompute(img1, None)                                #draw detection points
kp2, des2 = orb.detectAndCompute(img2, None)                                #draw detection points

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)                       #Brute-force matcher

matches = bf.match(des1, des2)                                              #match key points
matches = sorted(matches, key = lambda x:x.distance)                        #sort the matched points    

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:100], None, flags=2)  #draw the matched points 

plt.imshow(img3)                                                            #display the image            
plt.colorbar()
plt.show()