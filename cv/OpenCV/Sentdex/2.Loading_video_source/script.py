import cv2
import numpy as np

#get camera
cap = cv2.VideoCapture(0)

#to save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

#loop to stream video
while True:
    #ret is boolean if frame is there, true, otherwise, false
    ret, frame = cap.read()
    #convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #save frame
    out.write(frame)
    #show both frames
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    #if key pressed and key is 'q', exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release camera
cap.release()
#release saving resources
out.release()
#destroy window
cv2.destroyAllWindows()
