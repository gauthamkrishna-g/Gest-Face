import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobel_x = cv2.Sobel(frame, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(frame, cv2.CV_64F, 0, 1)
    canny_edge = cv2.Canny(frame, 50, 100)
    
    cv2.imshow("frame", frame)
    cv2.imshow("laplacian", laplacian)
    cv2.imshow("sobel_x", sobel_x)
    cv2.imshow("sobel_y", sobel_y)
    cv2.imshow("canny_edge", canny_edge)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
