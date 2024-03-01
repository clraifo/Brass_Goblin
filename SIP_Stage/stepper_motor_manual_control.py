import RPi.GPIO as GPIO
import time

# Define GPIO pins
DIR_PIN = 16
STEP_PIN = 17
STEPS_PER_REVOLUTION = 200

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

def step():
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)  # This delay might need adjustment
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)  # This delay might need adjustment

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
            rotate_motor(GPIO.HIGH, 2000, STEPS_PER_REVOLUTION // 2)  # Half revolution as example
        elif cmd == 'R':
            print("Rotating reverse")
            rotate_motor(GPIO.LOW, 2000, STEPS_PER_REVOLUTION // 2)  # Half revolution as example
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
        GPIO.cleanup()

