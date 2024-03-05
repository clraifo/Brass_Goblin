import RPi.GPIO as GPIO
import time

# Define GPIO pins based on wiring
DIR_PIN = 16  # Direction pin connected to GPIO 16
STEP_PIN = 17  # Step pin connected to GPIO 17
ENABLE_PIN = 23  # Enable pin connected to GPIO 23

# Constants for direction
CW = 1  # Clockwise rotation
CCW = 0  # Counter-clockwise rotation

STEPS = 96000  # Number of microsteps for the desired movement
STEP_DELAY = 0.00005  # Time between each step, adjust for your motor's speed & power supply

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

GPIO.output(ENABLE_PIN, GPIO.LOW)  # Enable the driver

def rotate_motor(steps, direction):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(STEP_DELAY)

try:
    # Move 96k steps clockwise
    rotate_motor(STEPS, CW)
    
    # Short pause
    time.sleep(1)
    
    # Move 96k steps counter-clockwise
    rotate_motor(STEPS, CCW)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Disable the driver
    GPIO.cleanup()  # Clean up GPIO

print("Completed the movements.")
