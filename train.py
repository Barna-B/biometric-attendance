import face_recognition
import os
import pickle

known_encodings = []
known_names = []

dataset_path = "dataset"

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(person)

print("Training complete!")

# Save data
with open("encodings.pkl", "wb") as f:
    pickle.dump((known_encodings, known_names), f)