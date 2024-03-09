import RPi.GPIO as GPIO

# Define the GPIO pin that the LED is connected to
LED_PIN = 18  # Example GPIO pin

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)

# Create a PWM instance on the LED pin at 100 Hz
pwm = GPIO.PWM(LED_PIN, 100)

# Start PWM with a specific duty cycle to set the brightness
duty_cycle = 50  # Set the brightness level (0 to 100)
pwm.start(duty_cycle)

# The LED will now maintain the set brightness level indefinitely
# until the script is interrupted or the program stops

try:
    # Just keep the script running to maintain LED brightness
    while True:
        pass  # Do nothing

except KeyboardInterrupt:
    # Handle the Ctrl-C event to gracefully shutdown the PWM
    pass

finally:
    pwm.stop()      # Stop PWM
    GPIO.cleanup()  # Clean up GPIO
