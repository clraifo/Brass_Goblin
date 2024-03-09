# reflects 1/16 step resolution 

from picamera import PiCamera
import RPi.GPIO as GPIO
import time

# GPIO pin setup based on your hardware configuration
DIR_PIN = 16
STEP_PIN = 17
ENABLE_PIN = 23

# Stepper motor configuration
CW = 1     # Clockwise Rotation
CCW = 0    # Counter-clockwise Rotation
STEPS_FOR_2_25_INCHES = 96000  # Number of microsteps to move 2.25 inches

# Initialize the camera
camera = PiCamera()
camera.resolution = (1024, 768)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

GPIO.output(ENABLE_PIN, GPIO.LOW)  # Enable the stepper motor

def rotate_motor(direction, steps, delay=0.00005):  # Adjust delay for optimal speed and performance
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

def main():
    try:
        image_counter = 1
        while True:
            # Capture and save the image
            camera.capture(f'/home/clraifo/camera/training_images{image_counter:03d}.jpg')
            print(f"Image captured: headstamp{image_counter:03d}.jpg")

            # Move the block 2.25 inches to allow the case to fall
            rotate_motor(CW, STEPS_FOR_2_25_INCHES)
            
            # Move back to the starting position
            rotate_motor(CCW, STEPS_FOR_2_25_INCHES)

            image_counter += 1  # Prepare for the next case

            if input("Press Enter to continue or 'q' to quit: ").lower() == 'q':
                break

    except KeyboardInterrupt:
        print("Program stopped by user.")
    finally:
        GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Disable the stepper motor
        GPIO.cleanup()

if __name__ == "__main__":
    main()
