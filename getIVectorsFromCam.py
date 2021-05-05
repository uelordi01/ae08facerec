import face_recognition
import cv2
def put_text(image,  lista):
    # str_list = list(map(str, lista))
    # separator = ","
    text = ""
    counter = 0
    for l in lista:
        if counter % 10 == 0:
            text = text + "\n"
        text = text + "," + str(l)
        counter = counter + 1
    # str_output = separator.join(str_list)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # fontScale
    fontScale = 0.1

    # Red color in BGR
    color = (0, 0, 255)
    pos = (0, 400)
    # Line thickness of 2 px
    thickness = 2

    # Using cv2.putText() method
    image = cv2.putText(image, text, pos, font, fontScale,
                        color, thickness, cv2.LINE_AA, False)

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame, model="hog")
    if face_locations:
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        #put_text(frame, face_encodings)
        print("face_encodings {}".format(face_encodings))
    cv2.imshow("face_detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
