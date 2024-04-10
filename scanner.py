import cv2                                #pip install opencv-python
from pyzbar.pyzbar import decode          #pip install pyzbar

cam = cv2.VideoCapture(0)
address ='http://.../video' #replace dots with actual local IP of camera
cam.open(address)

n = 1
while True:
    n += 1
    success, frame = cam.read()

    if n % 10 == 0:               #Scans for QR code every 10th iteration of loop (about every 0.36s)
        for i in decode(frame):
            print(i.data.decode('UTF-8'))
    
    cv2.imshow('Scanner', frame)  #Opens window to see the screen, can be removed if you just want the functionality without the window
    cv2.waitKey(1)

