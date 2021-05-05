import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
capture = False
while True:
    ret, frame = video_capture.read()
    #cv2.namedWindow('Object Tracker')
    cv2.imshow("current_frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()