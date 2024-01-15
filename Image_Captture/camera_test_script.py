import time
from picamera import PiCamera

# Initialize the camera
camera = PiCamera()

# Set medium resolution (e.g., 1280x720)
camera.resolution = (1280, 720)
camera.start_preview()

# Delay for camera warm-up
time.sleep(2)

try:
    for i in range(100):  # Adjust the range for more/fewer images
        # Capture an image with medium quality
        camera.capture(f'/home/pi/image_{i:03d}.jpg', quality=20)
        time.sleep(0.5)  # Capture every half second
finally:
    camera.stop_preview()
