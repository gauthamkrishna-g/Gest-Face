import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Images", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("watchgray.jpg", img)

#plt.imshow(img, cmap='gray', interpolation='bicubic')
