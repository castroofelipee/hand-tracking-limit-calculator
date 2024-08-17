# Hand Tracking Mathematical Limit Calculator

This project demonstrates a hand tracking application using Python and Streamlit. The application simulates a mathematical limit problem based on hand gestures detected via a webcam. It leverages MediaPipe for hand tracking and integrates a mathematical limit calculator to show results based on specific hand movements.

![Demo Video](./assets/demo.webm)


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Configuration](#configuration)
- [Dependencies](#dependencies)

## Features
- Real-time hand tracking using MediaPipe.
- Gesture recognition to trigger mathematical limit calculations.
- Streamlit interface to display results and video feed.
- Customizable mathematical function for limit calculations.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/castroofelipee/hand-tracking-limit-calculator.git
   cd hand-tracking-limit-calculator

2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv environment
    source environment/bin/activate  
    ```

3. **Install Dependencies**
    ```bash 
    pip install -r requirements.txt
    ```

## Usage 

1. **Run the streamlit Application**
    ```python
    streamlit run app.py
    ```

2. **Interact the Streamlit Application**
    - Use the checkbox in the Streamlit interface to start tracking
    - Show the specific hand gesture 
    - The limit value will be displayed when the corresponding gesture is detected


# File Structure
    |- environment                  # Virtual environment directory
    |- src
    |- components
        |- calculator.py          # Mathematical limit calculation logic
        |- gesture_recognition.py # Gesture recognition logic
        |- hand_tracking.py       # Hand tracking using MediaPipe
    |- utils
        |- streamlit_helpers.py   # Helper functions for Streamlit
        |- app.py                 # Main Streamlit application
        |- config.py              # Configuration file

# File Descriptions
- calculator.py: Contains the LimitCalculator class for computing mathematical limits.
- gesture_recognition.py: Defines the GestureRecognition class for recognizing hand gestures.
- hand_tracking.py: Implements the HandTracker class for detecting and processing - hand landmarks using MediaPipe.
- streamlit_helpers.py: Includes helper functions for displaying video frames and limit values in Streamlit.
- app.py: Main entry point for the Streamlit application that ties together hand tracking and limit calculation.

## Configuration
- Modify `config.py` to adjust configuration parameters as needed

## Dependencies
- Python 3.7 or higher
- Streamlit
- OpenCV
- MediaPipe
- NumPy