import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

DIR = 20 #direction GPIO pin
STEP = 21 # step GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# define number of steps
steps = 200

# rotate the motor function
def rotate_motor(direction, steps):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.setup(STEP, GPIO.LOW)
    
# rotate the motor
rotate_motor(GPIO.HIGH, steps)

GPIO.cleanup()
