import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
capture = False
counter = 0
while True:
    ret, frame = video_capture.read()
    #cv2.namedWindow('Object Tracker')
    cv2.imshow("current_frame",frame)
    counter = counter +1
    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == 82 or key == 115:
        path = "db"
        cv2.imwrite("db/image"+str(counter)+".jpg", frame)
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()