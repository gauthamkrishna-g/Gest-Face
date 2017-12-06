import cv2
import numpy as np

img = cv2.imread('download.jpeg')
ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

im2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(im2gray, 10, 255, cv2.THRESH_BINARY)
adaptive_threshold = cv2.adaptiveThreshold(im2gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                           cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('adaptive', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
