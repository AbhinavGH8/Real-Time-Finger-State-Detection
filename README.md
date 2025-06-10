# Real-Time-Finger-State-Detection
A very simple Python program that uses your webcam to detect hand movements and count raised fingers in real-time. Built with OpenCV and MediaPipe, it tracks 21 hand landmarks and identifies whether each finger is up or down.
It also identifies simple gestures such as a Wave 👋 ( Five fingers up) , Peace ✌️ ( Middle and index fingers up) , 🤟 (Index , Thumb and Pinky up)

## **Features** ✨
- Tracks 21 hand landmarks in real-time
- Detects if each finger (thumb to pinky) is **up** or **down**
- Counts total raised fingers
- Visualizes hand connections with colored landmarks

## **How It Works** 🔍
1. Uses MediaPipe's hand landmark model to detect hands
2. Compares landmark positions to determine finger states
3. Displays results live with OpenCV

## **Installation** ⚙️
```bash
pip install opencv-python mediapipe

##Future Ideas 💡
Add gesture recognition (👍, ✌️)

Control apps with hand movements

Build a virtual mouse

Tech Stack 🛠️
Python 3

OpenCV (for camera/video processing)

MediaPipe (for hand tracking)

Made by Abhinav S
BTech Student | AI/ML Student

