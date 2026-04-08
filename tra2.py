import face_recognition
import os
import pickle

# Folder where all faces are saved
dataset_dir = os.path.expanduser("~/biometric_dataset")

known_encodings = []
known_names = []

# Go through each person's folder
for person in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person)

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(person)
        else:
            print(f"No face found in {image_path}")

# Save encodings to file
with open("encodings.pkl", "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("Training complete! Encodings saved to encodings.pkl")