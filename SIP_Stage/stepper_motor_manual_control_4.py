import RPi.GPIO as GPIO
import time

# Define GPIO pins
DIR_PIN = 16
STEP_PIN = 17
ENABLE_PIN = 23  # Define the pin connected to the A4988's "Enable" pin
STEPS_PER_REVOLUTION = 3200  # For 1/16 microstep resolution

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

GPIO.output(ENABLE_PIN, GPIO.LOW)  # Enable the driver by setting the pin low

def step(delay):
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(delay)  # Adjust this delay for smoother operation
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(delay)  # Consistent delay for high and low states

def rotate_motor(direction, delay, steps):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        step(delay / 1000000.0)  # Convert delay from microseconds to seconds for accurate timing

def user_control():
    while True:
        cmd = input("Enter command ([F]orward, [R]everse, [S]top, [Q]uit): ").upper()
        if cmd in ['F', 'R']:
            speed_cmd = input("Choose speed ([1] Fast, [2] Slow): ").upper()
            delay = 0.001 if speed_cmd == '1' else 0.005  # Fast or slow operation
            direction = GPIO.HIGH if cmd == 'F' else GPIO.LOW
            print("Rotating", "forward" if cmd == 'F' else "reverse", "at", "fast" if speed_cmd == '1' else "slow", "speed")
            GPIO.output(ENABLE_PIN, GPIO.LOW)  # Ensure the driver is enabled
            rotate_motor(direction, delay, STEPS_PER_REVOLUTION)  # Rotate one full revolution
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
