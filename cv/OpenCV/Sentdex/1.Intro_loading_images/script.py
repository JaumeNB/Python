import cv2
import numpy as np
import matplotlib.pyplot as plt

#load an image with opencv
img = cv2.imread('cat400x400.png', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR
#IMREAD_UNCHANGED

#show image with opencv
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#see image with matplotlib, useful to see pixels and plot on top
plt.imshow(img, cmap='gray', interpolation = 'bicubic')
plt.show()

#save image
cv2.imwrite('saved_image.png', img)
