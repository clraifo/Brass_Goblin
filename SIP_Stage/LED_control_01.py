import RPi.GPIO as GPIO
import time

# Define the GPIO pin that the LED is connected to
LED_PIN = 18  # Example GPIO pin

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)

# Create a PWM instance on the LED pin at 100 Hz
pwm = GPIO.PWM(LED_PIN, 100)

# Start PWM with 0% duty cycle (off)
pwm.start(0)

try:
    # Example: Increase brightness gradually
    for duty_cycle in range(0, 101, 1):  # Increment duty cycle from 0% to 100%
        pwm.ChangeDutyCycle(duty_cycle)  # Change the duty cycle
        time.sleep(0.02)  # Wait for 20ms

    # Keep the LED on at full brightness for a second
    time.sleep(1)

    # Example: Decrease brightness gradually
    for duty_cycle in range(100, -1, -1):  # Decrement duty cycle from 100% to 0%
        pwm.ChangeDutyCycle(duty_cycle)  # Change the duty cycle
        time.sleep(0.02)  # Wait for 20ms

finally:
    pwm.stop()      # Stop PWM
    GPIO.cleanup()  # Clean up GPIO

