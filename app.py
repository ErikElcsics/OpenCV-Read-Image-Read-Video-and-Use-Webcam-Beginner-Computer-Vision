# Read Image
# Loads an image file and displays it in a window. Press any key to close the image window.

import cv2  # Import the OpenCV library

# Load an image from a file using cv2.imread(). Make sure the path is correct.
img = cv2.imread("Assets/MyImage.png")

# Display the loaded image in a window titled "This is my image"
cv2.imshow("This is my image", img)

# Wait for a key press indefinitely (0 means infinite wait)
cv2.waitKey(0)



# Read Video
# Loads a video file and displays it frame by frame. It keeps looping until the video ends or you press 'q' to quit.

# Set the width and height you want to resize each video frame to
frameWidth = 640
frameHeight = 480

# Load a video from file
cap = cv2.VideoCapture("Assets/Any_video.mp4")

# Continuously read frames from the video
while True:
    success, img = cap.read()  # Read a frame from the video
    if not success:
        break  # Exit the loop if video ends or cannot be read

    # Resize the frame to the desired width and height
    img = cv2.resize(img, (frameWidth, frameHeight))

    # Display the current video frame
    cv2.imshow("Result", img)

    # If the user presses the 'q' key, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Read Webcam
# Accesses your computer’s webcam, captures video in real-time, and displays it. You can exit the video feed by pressing 'q'.

# Set desired frame width and height
frameWidth = 640
frameHeight = 480

# 0 refers to the default webcam (built-in or first connected camera)
cap = cv2.VideoCapture(0)

# Set the width (property 3), height (property 4), and brightness (property 10)
cap.set(3, frameWidth)      # Set width
cap.set(4, frameHeight)     # Set height
cap.set(10, 150)            # Set brightness level

# Continuously capture frames from the webcam
while True:
    success, img = cap.read()  # Read a frame from the webcam

    # Display the frame in a window
    cv2.imshow("Result", img)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
