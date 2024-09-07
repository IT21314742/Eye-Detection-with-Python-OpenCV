import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade 

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()