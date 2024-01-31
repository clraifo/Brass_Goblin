import cv2

def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # '0' is usually the default value for the first camera

    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    try:
        # Capture one frame
        ret, frame = cap.read()

        if ret:
            # Display the captured image
            cv2.imshow('Camera Test', frame)
            cv2.waitKey(0)  # Wait for a key press to close the window
        else:
            print("Error: No frame captured")

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_image()
