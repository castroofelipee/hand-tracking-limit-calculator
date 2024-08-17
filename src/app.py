import streamlit as st
import cv2
from components.hand_tracking import HandTracker
from components.gesture_recognition import GestureRecognition
from components.calculator import Calculator
from utils.streamlit_helpers import capture_frame


def main():
    st.title("Hand Tracking Mathematical Limit Simulator")

    if "stop_button_clicked" not in st.session_state:
        st.session_state.stop_button_clicked = False

    hand_tracker = HandTracker()
    gesture_recognizer = GestureRecognition()
    calculator = Calculator()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Cannot open camera")
        return

    stframe = st.empty()
    if st.button("Stop", key="stop_button"):
        st.session_state.stop_button_clicked = True

    while cap.isOpened() and not st.session_state.stop_button_clicked:
        frame = capture_frame(cap)
        if frame is None:
            break

        results = hand_tracker.process_frame(frame)
        frame = hand_tracker.draw_landmarks(frame, results)

        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            if gesture_recognizer.recognize_gesture(landmarks):

                result = calculator.calculate_limit()
                calculation_text = f"Limit as x -> ∞: {result}"
                cv2.putText(
                    frame,
                    calculation_text,
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

        stframe.image(frame, channels="BGR")

    cap.release()


if __name__ == "__main__":
    main()


# by Felipe Castro, 17 aug 2024