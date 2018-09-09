import numpy as np
import cv2

#load image
img1 = cv2.imread('image.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

#sum images
add = img1 + img2
#sum images with weights
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows,cols,channels = img2.shape

print (rows, cols, channels)

#convert image to grayscale
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# pixels between 220 and 255 converted to white (255)
# otherwise to black (0) and stored to mask
ret,mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
#invert mask
mask_inv = cv2.bitwise_not(mask)

#make apples placeholder in cat backgraound image
img1_gb = cv2.bitwise_and(img1, img1, mask = mask_inv)

#crop apples in apple picture that fits exactly with previous
#placeholder
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_gb, img2_fg)

#show image with opencv
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_gb', img1_gb)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
