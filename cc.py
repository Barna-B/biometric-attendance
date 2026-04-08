import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Important!
if not cam.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Test Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cam.release()
cv2.destroyAllWindows()