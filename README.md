# 👤 Real-Time AI Face Recognition Attendance System

## 📌 Project Overview
This project is an AI-based Face Recognition Attendance System that automatically detects and recognizes faces in real-time using a webcam and marks attendance in a CSV file. It uses Deep Learning and Computer Vision techniques to identify individuals from a pre-trained dataset. The system captures live video, detects faces, matches them with stored encodings, and records attendance automatically.

## 🚀 Features
- 🎥 Real-time face detection using webcam  
- 🧠 AI-based face recognition using DeepFace  
- 📂 Dataset-based training system  
- 📝 Automatic attendance marking in CSV file  
- 👥 Supports multiple users  
- ⚡ Fast real-time processing  
- 💾 Encoded face storage for quick recognition  
- 🔄 Works with dynamic dataset updates  

## 🏗️ Project Structure
FaceAttendanceSystem/
│
├── dataset/               # Training images (person-wise folders)  
├── encode_faces.py        # Script to encode dataset faces  
├── main.py                # Runs real-time attendance system  
├── encodings.pkl          # Saved face encodings  
├── attendance.csv         # Attendance records  
├── requirements.txt       # Python dependencies  
└── README.md  

## ⚙️ Installation
1. Clone the repository:
git clone https://github.com/venkatesh915/FaceAttendanceSystem.git  
cd FaceAttendanceSystem  

2. Install dependencies:
pip install -r requirements.txt  

## ▶️ How to Run Project
Step 1: Add dataset images  
dataset/
   person_name/
      image1.jpg
      image2.jpg  

Step 2: Encode faces  
python encode_faces.py  

Step 3: Run system  
python main.py  

Press Q to exit camera.

## 🧠 Tech Stack
Python, OpenCV, DeepFace, TensorFlow, NumPy

## 📊 Output
- Live face detection  
- Name display on recognized face  
- Attendance saved in CSV file  

## 📌 Future Improvements
- Web dashboard using Flask  
- Excel report generation  
- Mobile app integration  
- Cloud database storage  
- Faster AI models  

## 👨‍💻 About Me
Name: Boddu Venkateswara Rao  
Course: B.Tech AIML Student  
Interest: AI, Machine Learning, Data Science, Computer Vision  
Email: venkateshboddu923@gmail.com  
LinkedIn: https://www.linkedin.com/in/venkateswara-rao-boddu-747474302?utm_source=share_via&utm_content=profile&utm_medium=member_android
GitHub: https://github.com/venkatesh915  

## ⭐ Support
If you like this project, give it a star on GitHub.

## 📜 License
This project is for educational purposes only.
