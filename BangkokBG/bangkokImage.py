import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*"XVID")

output_file = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

cap = cv2.VideoCapture(0)

time.sleep(2)

bg = 0

image = cv2.imread("Bangkok.jpeg")

while (cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame,(640, 480))
    image = cv2.resize(frame,(640,480))
    if not ret:
        break
    img = np.flip(image,axis = 1)

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    upper_black = np.array([104,153,70])
    lower_black = np.array([30,30,0])
    mask = cv2.inRange(hsv,lower_black,upper_black)
    res = cv2.bitwise_and(frame,frame, mask = mask)

    f = frame - res
    f= np.where(f == 0, image, f)

    


