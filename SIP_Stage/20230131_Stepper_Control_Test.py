import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
dir_pin = 20  # Direction pin
step_pin = 21  # Step pin
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

# Set the rotation direction
def set_direction(clockwise=True):
    GPIO.output(dir_pin, clockwise)

# Single step
def step():
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(0.001)  # Adjust this delay for speed control
    GPIO.output(step_pin, GPIO.LOW)
    time.sleep(0.001)

# Perform steps
def move_steps(steps, clockwise=True):
    set_direction(clockwise)
    for _ in range(steps):
        step()

# Example usage
try:
    steps = 200  # Change this to match your motor's steps per revolution
    move_steps(steps, True)  # Move clockwise
    time.sleep(1)
    move_steps(steps, False)  # Move counterclockwise
    
finally:
    GPIO.cleanup()
