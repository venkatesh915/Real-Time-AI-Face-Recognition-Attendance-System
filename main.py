import cv2
import numpy as np
import pickle
from deepface import DeepFace
from datetime import datetime

# -----------------------------
# LOAD ENCODINGS
# -----------------------------
print("✅ Loading encodings...")

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

names = data["names"]

print("🎥 Camera started... Press Q to exit")

# -----------------------------
# ATTENDANCE
# -----------------------------
def mark_attendance(name):
    with open("attendance.csv", "a+") as f:
        f.seek(0)
        lines = f.readlines()
        existing = [line.split(",")[0] for line in lines]

        if name not in existing:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{name},{now}\n")

# -----------------------------
# CAMERA
# -----------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # 🔥 DeepFace detection (NO dlib errors)
        result = DeepFace.extract_faces(
            img_path=frame,
            detector_backend="opencv",
            enforce_detection=False
        )

        for face in result:
            facial_area = face["facial_area"]

            x = facial_area["x"]
            y = facial_area["y"]
            w = facial_area["w"]
            h = facial_area["h"]

            # Crop face
            face_img = frame[y:y+h, x:x+w]

            # Compare with database
            try:
                df = DeepFace.find(
                    img_path=face_img,
                    db_path="dataset",
                    enforce_detection=False
                )

                if len(df[0]) > 0:
                    name = df[0].identity.iloc[0].split("\\")[1]

                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, name, (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    mark_attendance(name)

            except:
                pass

    except Exception as e:
        print("⚠️ Error:", e)

    cv2.imshow("Face Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()