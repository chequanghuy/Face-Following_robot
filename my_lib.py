import math
import serial
import time

def distance(center, another_center):
    a = (center[0] - another_center[0])**2
    b = (center[1] - another_center[1])**2
    return math.sqrt(a+b)

def Uart_control(angle, COM):
    ser = serial.Serial(COM, 9800, timeout = 1)
    time.sleep(2)
    ser.write(angle)

n = 180
t = str(n)
value = bytes(t, 'utf-8')

Uart_control(value, 'COM10')