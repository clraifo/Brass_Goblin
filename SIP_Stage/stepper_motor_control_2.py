import RPi.GPIO as GPIO
import time

# Define GPIO pins
DIR_PIN = 16
STEP_PIN = 17
STEPS_PER_REVOLUTION = 200

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

# Function to perform a step
def step():
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)  # This delay might need adjustment
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)  # This delay might need adjustment

# Function to rotate motor
def rotate_motor(direction, delay, steps):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        step()
        time.sleep(delay / 1000000.0)  # Convert delay from microseconds to seconds

def loop():
    while True:
        # Set motor direction clockwise
        rotate_motor(GPIO.HIGH, 2000, STEPS_PER_REVOLUTION)
        time.sleep(1)  # Wait for 1 second

        # Set motor direction counterclockwise
        rotate_motor(GPIO.LOW, 1000, STEPS_PER_REVOLUTION)
        time.sleep(1)  # Wait for 1 second

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        GPIO.cleanup()  # Clean up GPIO to ensure a clean exit
