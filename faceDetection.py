# include lib
from my_lib import *  # using lib are make by myself
# include opencv and numpy
import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
#_____________________________  Repair something    ____________________________________#
cap = cv2.VideoCapture(0)                                       # read Camera
cap.set(3,640)                                                  # set Width
cap.set(4,480)                                                  # set Height
Center = (320, 240)                                             # Center camera
center_of_Face = (0,0)                                          # khai báo mảng chứa tọa độ tâm khuôn mặt đang theo

ser = Init_uart('COM12')                                        # Init Uart-Protocol at COM.. to communitive with another MCU

#----------------------------------     Main     ----------------------------------------#

center_of_Face = MouseCallBack('video', cap, faceCascade)
print(center_of_Face)
while True: 
    ret, img = cap.read()                                       # đọc Camera
    img = cv2.flip(img, 1)                                     # Xoay Camera
#_________________________________  Face detection  ____________________________________#
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
#________________________________________________________________________________________#
    minz = 99999
    if faces == ():
        cv2.imshow('video',img)
    else:
        face_centers = ((0,0), (0,0))
        face = (0,0)
        for (x,y,w,h) in faces :
            a = (int(x + w/2), int(y + h/2))
            b = distance(center_of_Face, a)
            if (b < minz) :
                minz = b
                face_centers = ((x,y), (x+w,y+h))
                face = a
        
        if abs(face[0] - Center[0]) > 10 :
            print('lech ngang')
            print(abs(face[0] - Center[0]))
            # cv2.imshow('video',img)
            if face[0] - Center[0] > 0 :
                # xoay phải
                Angle(ser,1)
            if face[0] - Center[0] < 0 :
                # xoay trái
                Angle(ser,2)

        if abs(face[1] - Center[1]) > 10 :
            print('lech')
            print(abs(face[1] - Center[1]))
            # cv2.imshow('video',img)
            if face[1] - Center[1] > 0:
                # xoay xuống
                Angle(ser,3)
            if face[1] - Center[1] < 0:
                # xoay lên
                Angle(ser,4)

        cv2.rectangle(img,face_centers[0],face_centers[1],(255,0,0),2)
        center_of_Face = face
        # print(center_of_Face)
        cv2.line(img, center_of_Face, Center, (0, 255, 0), 5)
        cv2.imshow('video',img)

    if cv2.waitKey(30) & 0xff == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
