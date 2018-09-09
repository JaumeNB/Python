import numpy as np
import cv2

#load image
img = cv2.imread('image.png', cv2.IMREAD_COLOR)

#take pixel and modify it
px = img[55,55]
px = [255,255,255]
print (px)

#ROI:region of image (set of pixels in an image)
#convert them to white
img[100:150, 100:150]= [255, 255, 255]

#show image with opencv
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
