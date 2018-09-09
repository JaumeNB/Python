import numpy as np
import cv2

#load image
img = cv2.imread('bookpage.jpg', cv2.IMREAD_COLOR)

#apply threshold: above threshold 12 will be 255, below will be 0
#threshold to use. Threshold being applied over RGB image
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#apply same threshold to grayscaled image
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

#apply gaussian over grayscaled image
gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#show image with opencv
cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold from gray', threshold2)
cv2.imshow('threshold gauss', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
