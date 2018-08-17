#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:50:50 2018

@author: root1
"""

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")             #read the face cascade file
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")                              #read the eye cascade file
watch_cascade = cv2.CascadeClassifier("cascade.xml")                                    #read the object cascade file

cap = cv2.VideoCapture(0)                                           

while True:
    ret, img = cap.read()                                                               #read the image from the webcam    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                        #convert the image into grayscale    
    faces = face_cascade.detectMultiScale(gray)                                         #detect faces    
    
    watches = watch_cascade.detectMultiScale(gray, 40, 40)                              #detect watch

    for (x, y, w, h) in watches:
        font = cv2.FONT_HERSHEY_SIMPLEX                                                 
        cv2.putText(img, "watch", (x-w, y-h), (255,255,0), 2, cv2.LINE_AA)              
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)                           #draw a rectange around watch
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)                             #draws a rectangle around face
        roi_gray = gray[y:y+h, x:x+w]   
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)                                   #matches eye cascade    
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)            #draw rectangle around eye
            
    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()