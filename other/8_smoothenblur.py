import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lower_red = np.array([100, 50, 80])
    #higher_red = np.array([200, 200, 200])
    
    lower_red = np.array([150, 150, 50])
    higher_red = np.array([180, 255, 150])
    
    mask = cv2.inRange(hsv, lower_red, higher_red)
    final = cv2.bitwise_and(frame, frame, mask=mask)
    
    kernel = np.ones((15, 15), np.float32) / 255
    smoothed = cv2.filter2D(final, -1, kernel)
    gaus_blur = cv2.GaussianBlur(final, (15, 15), 0)
    med_blur = cv2.medianBlur(final, 15)
    bi_blur = cv2.bilateralFilter(final, 15, 15, 75)

    cv2.imshow("frame", frame)
    cv2.imshow("smoothed", smoothed)
    cv2.imshow("gaussian blur", gaus_blur)
    cv2.imshow("medina blur", med_blur)
    cv2.imshow("bi blur", bi_blur)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
cap.release()    
