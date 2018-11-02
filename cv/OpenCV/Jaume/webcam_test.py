import cv2

#get camera
cap = cv2.VideoCapture(0)

#loop to stream video
while True:
    #ret is boolean if frame is there, true, otherwise, false
    ret, frame = cap.read()
    #show both frames
    cv2.imshow('frame', frame)
    #if key pressed and key is 'q', exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release camera
cap.release()
#destroy window
cv2.destroyAllWindows()
