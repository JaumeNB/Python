import cv2
import numpy as np

cap = cv2.VideoCapture(1)

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
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(mask_final, cv2.MORPH_OPEN, kernel)
    #erosion = cv2.erode(mask_final,kernel,iterations = 1)
    """smoothing with median blur"""
    median = cv2.medianBlur(opening, 15)
    """and operation to show color red only"""
    res = cv2.bitwise_and(frame, frame, mask = median)

    #15x15 kernel to average pixel with its surroundings
    #kernel = np.ones((15, 15), np.float32)/225
    #smoothed = cv2.filter2D(res, -1, kernel)
    #blur = cv2.GaussianBlur(res, (15, 15), 0)
    #median = cv2.medianBlur(res, 15)

    #erosion = cv2.medianBlur(erosion, 15)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask_final)
    #cv2.imshow('opening',opening)
    #cv2.imshow('smoothed',smoothed)
    #cv2.imshow('blur',blur)
    #cv2.imshow('median',median)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
