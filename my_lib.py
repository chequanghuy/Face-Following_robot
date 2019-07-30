import math
import serial
import time
import cv2

def distance(center, another_center):
    a = (center[0] - another_center[0])**2
    b = (center[1] - another_center[1])**2
    return math.sqrt(a+b)

def Init_uart(COM):
    ser = serial.Serial(COM, 9600, timeout = 1)
    time.sleep(2)
    return ser
    
def Angle(ser,angle_real):
    if angle_real < 0 :
        angle_real1 = - angle_real + 180
    angle_send = chr(angle_real)
    value = bytes(angle_send, 'utf-8')
    ser.write(value)

def Mouse_event(event, x, y, f, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_event.x0 = x
        Mouse_event.y0 = y
        Mouse_event.draw = True
    if event == cv2.EVENT_LBUTTONUP:
        Mouse_event.x1 = x
        Mouse_event.y1 = y
        Mouse_event.draw = False
        miny = min(Mouse_event.y0,Mouse_event.y1)
        maxy = max(Mouse_event.y0, Mouse_event.y1)

        minx = min(Mouse_event.x0, Mouse_event.x1)
        maxx = max(Mouse_event.x0, Mouse_event.x1)
        Mouse_event.img = img[miny:maxy,minx:maxx]
    if event == cv2.EVENT_MOUSEMOVE:
        Mouse_event.x = x
        Mouse_event.y = y

Mouse_event.img = None
Mouse_event.x0 =0
Mouse_event.y0 =0
Mouse_event.x1 =0
Mouse_event.y1 =0
Mouse_event.x =0
Mouse_event.y =0
Mouse_event.draw = False

def MouseCallBack(video, cap, faceCascade):
    while True:
        ret , img = cap.read()
        img_lone = img.copy()
        if Mouse_event.draw:
            img_lone = cv2.rectangle(img_lone,(Mouse_event.x0,Mouse_event.y0),(Mouse_event.x,Mouse_event.y),(0,0,255),2)
        if Mouse_event.img is not None:
            check, a = check_faces(Mouse_event.img, faceCascade)
            if  check == False:
                pass
            else:
                return a

        cv2.imshow(video, img_lone)
        cv2.setMouseCallback(video, Mouse_event,img)

        if cv2.waitKey(int (1)) == ord('q'):
            break

def check_faces(img, faceCascade):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    if faces == ():
        return False, (0, 0)
    else:
        x, y, w, h = faces[0]
        a = (int(x + w/2), int(y + h/2))
        return True, a
    

    