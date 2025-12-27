import cv2
import numpy as np
import csv
import os
from datetime import datetime

# ---------- LOAD TRAINED MODEL ----------
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# ---------- LOAD FACE CASCADE ----------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------- ID TO NAME ----------
names = {
    1: "Rethikaa"   # Must match User ID used in capture_faces.py
}

# ---------- CAMERA ----------
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("❌ Camera not opening")
    exit()

# ---------- ATTENDANCE FILE ----------
if not os.path.exists("Attendance.csv"):
    with open("Attendance.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Date", "Time"])

marked_ids = set()

print("📷 Camera started. Press ESC to stop.")

while True:
    ret, frame = cam.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    # ✅ REMOVE MIRROR EFFECT
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:
        id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        print(f"DEBUG -> ID: {id_}, Confidence: {confidence}")

        if confidence < 95 and id_ in names:
            name = names[id_]

            if id_ not in marked_ids:
                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                with open("Attendance.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([id_, name, date, time])

                marked_ids.add(id_)

            label = f"{name}"
            color = (0, 255, 0)
        else:
            label = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cam.release()
cv2.destroyAllWindows()
print("✅ Program stopped successfully")
