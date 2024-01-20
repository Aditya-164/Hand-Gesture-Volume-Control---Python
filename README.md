# Hand-Gesture-Volume-Control---Python-Machine-Learning-project-COINCENT-MICROSOFT

Welcome to the **Hand Gesture Volume Control** project! This Python project leverages the power of machine learning and computer vision to create a hands-free, gesture-controlled audio volume adjustment system. This project was made by me while following the course on python - Machine Learning and AI by COINCENT and Microsoft. 

# The project utilizes the following key libraries:

- **unittest**: For unit testing.
- **cv2 (OpenCV)**: For image processing.
- **Mediapipe**: For hand tracking.
- **pycaw**: For controlling audio volume.

## Project Overview

### Purpose

The primary objective of this project is to enable users to control their computer's audio volume wirelessly through hand gestures captured by the computer's webcam. The implementation utilizes Mediapipe's hand tracking model to detect hand landmarks in real-time video frames, translating specific gestures into changes in the device's volume.

### Dependencies

Make sure you have the following libraries installed before running the project:

- unittest
- cv2
- Mediapipe
- pycaw

You can install these libraries using the following:

```bash
pip install unittest
pip install opencv-python
pip install mediapipe
pip install pycaw
```

### Project Workflow

1. **Initialize Audio Device**: The code sets up the audio device and initializes variables for volume control.

2. **Capture Video Feed**: It captures video from the default camera and prepares variables for drawing hand landmarks and detecting gestures.

3. **Hand Tracking Loop**:
   - Captures a frame from the video feed.
   - Converts the frame from BGR to RGB format for Mediapipe.
   - Detects hand landmarks using Mediapipe's hand-tracking model.
   - Extracts hand landmarks and calculates the distance between the thumb and index finger.
   - Maps the distance to a volume level using `numpy.interp()` and adjusts the audio volume         using `pycaw`.
   - Draws hand landmarks, distance measurement, and audio volume level on the video frame.
   - Displays the resulting video frame to the user.

4. **User Interface**:
   - Green circle indicates a valid gesture for volume control.
   - Displays current volume percentage and volume bar.
   - Shows the current frames per second (FPS) value.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Aditya-164/Hand-Gesture-Volume-Control---Python.git
cd Hand-Gesture-Volume-Control---Python
```

2. Install dependencies.

3. Run the project:

```bash
python HandGesture_VolControl.py
```

## Contributions and Issues

Contributions and bug reports are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/Aditya-164/Hand-Gesture-Volume-Control---Python/issues).

Enjoy wireless audio control with gestures! 🎵✋
