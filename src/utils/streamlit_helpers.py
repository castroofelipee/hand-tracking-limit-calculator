import streamlit as st


def display_frame(frame):
    st.image(frame, channels="BGR")


def capture_frame(cap):
    ret, frame = cap.read()
    return frame if ret else None
