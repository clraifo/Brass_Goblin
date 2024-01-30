import time
import picamera

# Number of images to capture
num_images = 100

# Delay between images in seconds
delay = 3  # 3 seconds

# Initialize the camera
with picamera.PiCamera() as camera:
    # Set camera resolution (optional, change as needed)
    camera.resolution = (1024, 768)

    for i in range(num_images):
        try:
            # Construct filename based on the iteration
            filename = f"image_{i:04d}.jpg"

            # Capture the image
            camera.capture(filename)

            # Print status message
            print(f"Captured {filename}")

            # Wait for a few seconds
            time.sleep(delay)

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop in case of an error

print("Image capture complete.")
