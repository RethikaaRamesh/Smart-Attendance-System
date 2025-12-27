📸 Smart Attendance System using Face Recognition
📌 Project Overview

The Smart Attendance System is a Python-based application that uses face recognition technology to automatically mark attendance.
It eliminates manual attendance, reduces proxy attendance, and improves accuracy by recognizing faces through a webcam.

This system captures facial images, trains a recognition model, and marks attendance in a CSV file when a registered face is detected.

🚀 Features

📷 Capture face images using webcam

🧠 Train face recognition model using LBPH algorithm

👤 Real-time face recognition

📝 Automatic attendance marking

❌ Unknown face detection

📊 Attendance stored in CSV file

🔄 Mirror image correction (natural camera view)

🛠 Technologies Used

Python 3.10

OpenCV (opencv-contrib-python)

NumPy

Haar Cascade Classifier

CSV file handling

Webcam (Computer Vision)

📂 Project Structure

Smart-Attendance-System/
│
├── capture_faces.py
│   └── Captures face images from webcam and stores them in the dataset
│
├── attendance.py
│   └── Trains the face recognition model using captured images
│
├── recognize_faces.py
│   └── Recognizes faces in real-time and marks attendance
│
├── haarcascade_frontalface_default.xml
│   └── Haar Cascade classifier for face detection
│
├── dataset/
│   └── Stores captured face images (user-wise folders)
│
├── trainer.yml
│   └── Saved trained LBPH face recognition model
│
├── Attendance.csv
│   └── Stores attendance records with date and time
│
└── README.md
    └── Project documentation and usage instructions

⚙️ Installation & Setup
1️⃣ Install Required Libraries
pip install opencv-contrib-python numpy

2️⃣ Capture Face Dataset

Run the following command and enter a numeric User ID:

python capture_faces.py


✔ Captures multiple images of your face
✔ Saves images in dataset/ folder

3️⃣ Train the Model
python attendance.py


✔ Trains the LBPH face recognition model
✔ Saves trained model as trainer.yml

4️⃣ Recognize Face & Mark Attendance
python recognize_faces.py


✔ Opens webcam
✔ Recognizes face
✔ Marks attendance in Attendance.csv
✔ Press Q to exit webcam

📊 Output

✅ Recognized face → Attendance marked

❌ Unknown face → Not marked

📁 Attendance stored in Attendance.csv

Example:

ID, Date, Time
1, 2025-01-02, 10:15:30

🧠 Algorithm Used

LBPH (Local Binary Pattern Histogram)
Chosen for its efficiency and accuracy in real-time face recognition systems.

🔐 Advantages

Prevents proxy attendance

Fast and accurate

Easy to use

Low-cost solution

Real-time detection

🔮 Future Enhancements

🔐 Login authentication

🌐 Web-based interface

☁️ Cloud database integration

📱 Mobile app support

🧾 Excel & database storage

👩‍💻 Developer

Rethikaa Ramesh
📧 Email: rethikaa05@gmail.com

🔗 GitHub: https://github.com/RethikaaRamesh

⭐ Conclusion

The Smart Attendance System is a practical and efficient solution for automating attendance using facial recognition, making it ideal for educational institutions and organizations.
