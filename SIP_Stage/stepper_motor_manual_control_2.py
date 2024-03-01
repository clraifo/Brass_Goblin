# this version includes the enable pin and sets it to high at the end of run time 
# which stops the motor from idling

import RPi.GPIO as GPIO
import time

# Define GPIO pins
DIR_PIN = 16
STEP_PIN = 17
ENABLE_PIN = 18  # Define the pin connected to the A4988's "Enable" pin
STEPS_PER_REVOLUTION = 200

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

GPIO.output(ENABLE_PIN, GPIO.LOW)  # Enable the driver by setting the pin low

def step():
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)  # Adjust this delay to control step speed
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)

def rotate_motor(direction, delay, steps):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        step()
        time.sleep(delay / 1000000.0)

def user_control():
    while True:
        cmd = input("Enter command ([F]orward, [R]everse, [S]top, [Q]uit): ").upper()
        if cmd == 'F':
            print("Rotating forward")
            GPIO.output(ENABLE_PIN, GPIO.LOW)  # Ensure the driver is enabled
            rotate_motor(GPIO.HIGH, 2000, STEPS_PER_REVOLUTION // 2)
        elif cmd == 'R':
            print("Rotating reverse")
            GPIO.output(ENABLE_PIN, GPIO.LOW)  # Ensure the driver is enabled
            rotate_motor(GPIO.LOW, 2000, STEPS_PER_REVOLUTION // 2)
        elif cmd == 'S':
            print("Motor stopped")
            GPIO.output(STEP_PIN, GPIO.LOW)
        elif cmd == 'Q':
            print("Exiting program")
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    try:
        user_control()
    except KeyboardInterrupt:
        print("\nProgram manually stopped")
    finally:
        GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Disable the driver to stop the motor
        GPIO.cleanup()  # Clean up GPIO to ensure a clean exit
