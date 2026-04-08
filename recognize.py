import cv2
import face_recognition
import pickle
from datetime import datetime

# Load trained data
with open("encodings.pkl", "rb") as f:
    known_encodings, known_names = pickle.load(f)

def mark_attendance(name):
    with open("attendance.csv", "a") as f:
        time = datetime.now().strftime("%H:%M:%S")
        date = datetime.now().strftime("%Y-%m-%d")
        f.write(f"{name},{date},{time}\n")

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb = frame[:, :, ::-1]

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding in encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)

        if True in matches:
            name = known_names[matches.index(True)]

            mark_attendance(name)

            cv2.putText(frame, name, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()