import math
import serial
import time

def distance(center, another_center):
    a = (center[0] - another_center[0])**2
    b = (center[1] - another_center[1])**2
    return math.sqrt(a+b)

def Init_uart(COM):
    ser = serial.Serial(COM, 9600, timeout = 1)
    time.sleep(2)
    return ser
    
def Angle(ser,angel_rc):
    angle_real=angel_rc
    if angle_real<0:
        angle_real=-angle_real+180
    angle_send=chr(angle_real)
    value = bytes(angle_send, 'utf-8')
    ser.write(value)