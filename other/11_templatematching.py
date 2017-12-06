import cv2
import numpy as np

img = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg', 0)
w, h = template.shape[::-1]

final = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
thresh = 0.75
loc = np.where(final > thresh)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)
    
cv2.imshow("img", img)
#cv2.imshow("loc", loc)
cv2.imshow("final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()
