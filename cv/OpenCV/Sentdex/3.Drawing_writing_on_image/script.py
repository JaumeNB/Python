import numpy as np
import cv2

#load image
img = cv2.imread('image.png', cv2.IMREAD_COLOR)

#write line in image: image, start point, end point,color, width
cv2.line(img, (0,0), (150, 150), (255, 0, 0), 15)

#write rectangle: image, top left coord, bottom right coord, color, width
cv2.rectangle(img, (15, 25), (250, 150), (0, 255, 0), 5)

#write a circle: image, center, radius, color, width (negative is circle filled)
cv2.circle(img, (100, 63), 55, (0,0,255), -1)

#write a polygon: define points, image, points, first and last point connected, color, width
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

#write: define font, image, phrase, location, font type, size, color, thickness
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Open cv trial', (0,130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

#show image with opencv
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
