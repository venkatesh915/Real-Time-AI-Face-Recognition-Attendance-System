import os
import pickle
import numpy as np
from deepface import DeepFace

dataset_path = "dataset"

encodings = []
names = []

print("🔄 Starting encoding with DeepFace...")

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    print("\n👤 Person:", person)

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        print("📸 Reading:", img_path)

        try:
            # 🔥 DeepFace generates embeddings (NO dlib, NO errors)
            embedding = DeepFace.represent(
                img_path=img_path,
                model_name="Facenet",
                enforce_detection=False
            )[0]["embedding"]

            encodings.append(embedding)
            names.append(person)

            print("🙂 Face encoded")

        except Exception as e:
            print("❌ Skipping:", img_path)
            print(e)

print("\n==========================")
print("Total encodings:", len(encodings))

data = {
    "encodings": encodings,
    "names": names
}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("✅ encodings.pkl created successfully!")
