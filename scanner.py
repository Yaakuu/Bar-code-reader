import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
address ='http://100.109.98.70:8080/video'
cam.open(address)

n = 1
while True:
    n += 1
    success, frame = cam.read()

    if n % 10 == 0:
        for i in decode(frame):
            print(i.data.decode('UTF-8'))
    
    cv2.imshow('Scanner', frame)
    cv2.waitKey(1)

