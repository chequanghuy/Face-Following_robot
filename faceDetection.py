# include lib
from my_lib import * # using lib are make by myself
# include opencv and numpy
import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)                                       #read Camera
cap.set(3,640)                                                  # set Width
cap.set(4,480)                                                  # set Height

center_of_Face = [0,0]                                                  # khai báo mảng chứa tọa độ tâm khuôn mặt đang theo

while True: 
    ret, img = cap.read()                                       # đọc Camera
#_________________________________  Face recognition____________________________________#
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                

    faces = faceCascade.detectMultiScale(
        gray ,
        scaleFactor=1.2 ,
        minNeighbors=5 ,     
        minSize=(20, 20)
    )
#_______________________________________________________________________________________#
    minz = 99999
    face_centers = ((0,0), (0,0))
    face = [0,0]
    for (x,y,w,h) in faces:
        a = [x + w/2, y + h/2]
        b = distance(center_of_Face, a)
        if (b < minz):
            minz = b
            face_centers = ((x,y),(x+w,y+h))
            face = a
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # print(x,y,w,h) 
    cv2.rectangle(img,face_centers[0],face_centers[1],(255,0,0),2)
    center_of_Face = face

    cv2.line(img, )
    cv2.imshow('video',img)
    print(img.shape) #240 - 320
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
