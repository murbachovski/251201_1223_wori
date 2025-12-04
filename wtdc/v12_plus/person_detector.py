
import cv2

# Initialize the HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open the video file
# Replace 'your_video.mp4' with the path to your video file.
# If you want to use a webcam, use 0 instead of the file path.
cap = cv2.VideoCapture('your_video.mp4')

while(cap.isOpened()):
    # Read the video frame by frame
    ret, frame = cap.read()

    if ret:
        # Detect people in the frame
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

        # Draw a rectangle around the detected people
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the output
        cv2.imshow('Person Detection', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
