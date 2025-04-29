# AI-Powered-Auto-Selfie-on-Smile-Detection
# SmileSnap 🤳😄
An AI-powered smile detection system that automatically captures a selfie when you smile using **MediaPipe**, **OpenCV**, and **Python**.

## 📸 Features
- Detects a face and measures smile using facial landmarks.
- Automatically takes a selfie when a smile is detected.
- Plays a sound after capturing the image.
- Saves images as `selfie_0.png`, `selfie_1.png`, etc.

## 🧠 How It Works
The system uses MediaPipe's **FaceMesh** to identify key facial landmarks. It calculates the distance between specific mouth corner points (landmarks `43` and `287`) to detect a smile. When the distance exceeds a threshold (88), it:
- Captures a selfie
- Plays a sound
- Saves the image

## 🛠️ Requirements
- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI (optional)
- Winsound (Windows only)

Install dependencies:
```bash
pip install opencv-python mediapipe pyautogui
