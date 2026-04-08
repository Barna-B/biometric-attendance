import cv2
import os
import time

# Ask for name
name = input("Enter your name: ").strip()

# Save folder in home directory
base_dir = os.path.expanduser("~")
dataset_dir = os.path.join(base_dir, "biometric_dataset")
person_dir = os.path.join(dataset_dir, name)
os.makedirs(person_dir, exist_ok=True)

# Open camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

print("Starting auto-capture of 10 images...")
count = 0

while count < 10:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Show the frame
    cv2.putText(frame, f"Capturing Image {count+1}/10", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Capture Face", frame)

    # Save the frame
    file_name = os.path.join(person_dir, f"{count}.jpg")
    saved = cv2.imwrite(file_name, frame)
    if saved:
        print(f"Saved successfully: {file_name}")
        count += 1
    else:
        print(f"Failed to save: {file_name}")

    # Wait 1 second between captures
    key = cv2.waitKey(1000) & 0xFF
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
print("Done capturing images!")