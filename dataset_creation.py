#tasted on python3
import numpy as np
import os
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

path = "D:\Projects\computer vision\FaceRecognition\"
 # path were u want store the data set
name = input('Enter user name:')

try:
    # Create target Directory
    os.makedirs(path+str(name))
    print("Directory " , path+str(name),  " Created ") 
except FileExistsError:
    print("Directory " , path+str(name) ,  " already exists")
sampleN=0;

while 1:

    ret, img = cap.read()
    frame = img.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        sampleN=sampleN+1;

        cv2.imwrite(path+str(name)+ "/" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.waitKey(100)

    cv2.imshow('img',img)

    cv2.waitKey(1)

    if sampleN > 40:

        break

cap.release()

cv2.destroyAllWindows()
