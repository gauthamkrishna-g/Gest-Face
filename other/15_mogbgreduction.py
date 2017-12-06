import numpy as np
import cv2

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
