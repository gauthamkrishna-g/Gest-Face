import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([150, 150, 50])
    higher_red = np.array([180, 255, 150])
    
    mask = cv2.inRange(hsv, lower_red, higher_red)
    final = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("final", final)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
cap.release()
