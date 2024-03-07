# uses 200 steps pre revolution

from picamera import PiCamera
import RPi.GPIO as GPIO
import time

# Adjust these constants to match your setup
DIR_PIN = 16  # Direction pin connected to GPIO 16
STEP_PIN = 17  # Step pin connected to GPIO 17
ENABLE_PIN = 23  # Enable pin connected to GPIO 23

# Setup for the stepper motor
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
# Steps might need adjustment based on your stepper motor's specification and microstepping settings
STEPS_FOR_2_25_INCHES = 9600  # Placeholder value, adjust according to your setup

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (1024, 768)  # Example resolution, adjust as needed

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Enable the stepper motor
GPIO.output(ENABLE_PIN, GPIO.LOW)

def rotate_motor(direction, steps, delay=0.005):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

def main_loop():
    try:
        image_counter = 1
        while True:
            input("Press Enter to capture an image and move the case...")
            # Capture image
            camera.capture(f'/home/pi/images/headstamp{image_counter:03d}.jpg')
            print(f'Captured headstamp{image_counter:03d}.jpg')
            
            # Move the block 2.25 inches clockwise to drop the case
            rotate_motor(CW, STEPS_FOR_2_25_INCHES)
            # Move the block 2.25 inches counterclockwise to return
            rotate_motor(CCW, STEPS_FOR_2_25_INCHES)
            
            image_counter += 1  # Prepare for the next image capture
    except KeyboardInterrupt:
        print("Program stopped by user.")
    finally:
        GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Disable the stepper motor
        GPIO.cleanup()  # Cleanup the GPIO

if __name__ == "__main__":
    main_loop()
