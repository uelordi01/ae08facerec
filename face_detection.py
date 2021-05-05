import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)
capture = False
while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame, model="hog")
    if face_locations:
        cv2.rectangle(frame, (face_locations[0][3], face_locations[0][0]), (face_locations[0][1], face_locations[0][2]), (255,0,0), 2)
    cv2.imshow("face_detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
