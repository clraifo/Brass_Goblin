import RPi.GPIO as GPIO
import subprocess
import time

# Stepper Motor Setup
DIR = 20        # Direction GPIO Pin
STEP = 21       # Step GPIO Pin
CW = 1          # Clockwise Rotation
CCW = 0         # Counterclockwise Rotation
SPR = 200 * 16  # Steps per Revolution adjusted for 1/16 microstepping

# Define microstepping pins and their GPIO setup if necessary
# MS1 = XX
# MS2 = XX
# MS3 = XX
# GPIO.setup([MS1, MS2, MS3], GPIO.OUT)
# GPIO.output([MS1, MS2, MS3], GPIO.HIGH)  # Setting for 1/16 microstepping

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Assuming 1/16 microstepping, adjust steps_per_inch accordingly
steps_per_inch = 100 * 16  # Adjust this value based on your actual steps per inch at 1/16 microstepping

def rotate_stepper(direction, steps, delay=0.0005):  # Adjusted delay for microstepping
    GPIO.output(DIR, direction)
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)

def capture_image(image_number):
    filename = f"/home/pi/camera/headstamp{image_number:03d}.jpg"
    cmd = f"raspistill -o {filename} -q 75"
    subprocess.run(cmd, shell=True)

image_number = 1
try:
    while True:
        user_input = input("Press 'Enter' to capture and rotate, or 'q' to quit: ").lower()
        if user_input == 'q':
            break

        capture_image(image_number)
        rotate_stepper(CW, int(2.25 * steps_per_inch))
        time.sleep(1)  # Adjust as needed
        rotate_stepper(CCW, int(2.25 * steps_per_inch))
        time.sleep(1)  # Adjust as needed
        image_number += 1

finally:
    GPIO.cleanup()
