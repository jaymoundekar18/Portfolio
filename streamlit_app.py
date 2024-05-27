import cv2
import streamlit as st
st.write("Hello!   this is JAY MOUNDEKAR")
# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the VideoCapture object was opened successfully
if not cap.isOpened():
    st.write("Error: Unable to open the camera")
    exit()

# Create a placeholder for the video feed
frame_placeholder = st.empty()

# Create a start button
start_btn = st.button("Start")

# Create a stop button
stop_button_pressed = False
stop_button = st.button("Stop")

# Check if the start button was clicked
if start_btn:
    # Loop to continuously read frames from the camera
    while True:
        # Read the next frame
        ret, frame = cap.read()

        # Check if the frame was read correctly
        if not ret:
            st.write("Error: Unable to read the next frame")
            break

        # Convert the frame from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in the placeholder
        frame_placeholder.image(frame, channels="RGB")

        # Check if the stop button was clicked
        if stop_button_pressed:
            break

        # Check if the stop button was clicked
        if stop_button:
            stop_button_pressed = True

    # Release the VideoCapture object and close any open OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

