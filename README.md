Here is a beginner-friendly version of code for Computer Vision - with explanations and detailed comments on how to Read Image, Read Video, and Use Webcam for someone just starting out!


# **Beginner Computer Vision - OpenCV: Read Image, Read Video, and Use Webcam**

### 👋 What is OpenCV?
**OpenCV (Open Source Computer Vision Library)** is an open-source library mainly aimed at real-time computer vision. It provides tools to process images and videos to identify objects, faces, or even handwriting of a human. You can use it with languages like Python, C++, and Java.

Now let’s look at how to use OpenCV to:
1. Read and display images.
2. Read and display videos.
3. Access and display webcam video in real-time.



## 🖼️ **Read Image**

python
import cv2  # Import the OpenCV library

# Load an image from a file using cv2.imread(). Make sure the path is correct.
img = cv2.imread("Assets/MyImage.png")

# Display the loaded image in a window titled "This is my image"
cv2.imshow("This is my image", img)

# Wait for a key press indefinitely (0 means infinite wait)
cv2.waitKey(0)


🔍 **Explanation**:  
This section loads an image file and displays it in a window. Press any key to close the image window.



## 🎞️ **Read Video**

python
import cv2  # Import OpenCV

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


🔍 **Explanation**:  
This section loads a video file and displays it frame by frame. It keeps looping until the video ends or you press **'q'** to quit.



## 🎥 **Read Webcam**
🔍 **Explanation**:  
This section accesses your computer’s webcam, captures video in real-time, and displays it. You can exit the video feed by pressing **'q'**.

python
import cv2  # Import OpenCV

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





