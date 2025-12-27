import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def getImagesAndLabels(path):
    faceSamples = []
    ids = []

    for file in os.listdir(path):
        if file.endswith(".jpg"):
            img_path = os.path.join(path, file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            id = int(file.split(".")[1])

            faces = detector.detectMultiScale(img)
            for (x, y, w, h) in faces:
                faceSamples.append(img[y:y+h, x:x+w])
                ids.append(id)

    return faceSamples, ids


faces, labels = getImagesAndLabels("dataset")

if len(faces) == 0:
    print("❌ No faces found. Please capture face images first.")
    exit()

recognizer.train(faces, np.array(labels))
recognizer.save("trainer.yml")
print("✅ Model trained successfully")
