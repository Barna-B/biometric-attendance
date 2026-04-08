# import cv2
# import os

# name = input("Enter your name: ")

# path = f"dataset/{name}"

# if not os.path.exists(path):
#     os.makedirs(path)

# cam = cv2.VideoCapture(0)
# count = 0

# while True:
#     ret, frame = cam.read()
#     cv2.imshow("Capture Face", frame)

#     key = cv2.waitKey(1)

#     if key == ord('s'):  # press 's' to capture
#         file_name = f"{path}/{count}.jpg"
#         cv2.imwrite(file_name, frame)
#         count += 1
#         print(f"Saved {file_name}")

#     elif key == ord('q'):  # press 'q' to quit
#         break

# cam.release()
# cv2.destroyAllWindows()








# import cv2
# import os

# name = input("Enter your name: ")

# path = f"dataset/{name}"

# if not os.path.exists(path):
#     os.makedirs(path)

# cam = cv2.VideoCapture(2, cv2.CAP_DSHOW)
# count = 0

# print("Press 's' to capture images, 'q' to quit")

# while True:
#     ret, frame = cam.read()

#     if not ret:
#         print("Failed to grab frame")
#         break

#     cv2.putText(frame, f"Images Captured: {count}", (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1,
#                 (0, 255, 0), 2)

#     cv2.imshow("Capture Face", frame)

#     key = cv2.waitKey(1) & 0xFF

#     if key == 13:  # Enter key
#         file_name = f"{path}/{count}.jpg"
#         cv2.imwrite(file_name, frame)
#         print(f"Saved {file_name}")
#         count += 1

#     elif key == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()




import cv2
import os

name = input("Enter your name: ").strip()

base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(base_dir, "dataset")
person_dir = os.path.join(dataset_dir, name)

os.makedirs(person_dir, exist_ok=True)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
count = 0

print("Press S to save, Q to quit")
print("Saving to:", person_dir)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.putText(frame, f"Images Captured: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(10) & 0xFF

    if key == ord('s'):
        file_name = os.path.join(person_dir, f"{count}.jpg")
        saved = cv2.imwrite(file_name, frame)

        print("Trying to save:", file_name)
        print("Saved successfully?" , saved)

        if saved:
            count += 1

    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
