import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """color filtering"""
    lower_red1 = np.array([0,70,50])
    upper_red1 = np.array([5,255,255])
    lower_red2 = np.array([175,70,50])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask_final = cv2.bitwise_or(mask1, mask2)
    """background false positives removal with opening"""
    kernel = np.ones((4,4),np.uint8)
    opening = cv2.morphologyEx(mask_final, cv2.MORPH_OPEN, kernel)
    #erosion = cv2.erode(mask_final,kernel,iterations = 1)
    """smoothing with median blur"""
    median = cv2.medianBlur(opening, 25)

    #laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    #sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges = cv2.Canny(median, 100, 200)

    cv2.imshow('original', frame)
    #cv2.imshow('median', median)
    #cv2.imshow('laplacian', laplacian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
