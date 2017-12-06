import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img,(0, 0), (200, 300), (255, 255, 255), 20)

cv2.rectangle(img, (20, 30), (200, 175), (0, 0, 255), 15)

cv2.circle(img, (100, 50), 63, (0, 255, 0), 1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1 ,1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hlooooh!', (10, 500), font, 6, (200, 255, 155), 13, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
