# This is a simple little snippet that I used to control an LED
# inside the chassis to provide lighting for the camera



import RPi.GPIO as GPIO

# Defines the GPIO pin that the LED is connected to
LED_PIN = 18  # Example GPIO pin

GPIO.setmode(GPIO.BCM)  # Uses Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)

# Creates a PWM instance on the LED pin at 100 Hz
pwm = GPIO.PWM(LED_PIN, 100)

# Starts PWM with a specific duty cycle to set the brightness
duty_cycle = 100  # Set the brightness level (0 to 100)
pwm.start(duty_cycle)

# The LED will now maintain the set brightness level indefinitely
# until the script is interrupted or the program stops

try:
    # Just keeps the script running to maintain LED brightness
    while True:
        pass  # Do nothing

except KeyboardInterrupt:
    # Handle the Ctrl-C event to gracefully shutdown the PWM
    pass

finally:
    pwm.stop()      # Stops PWM
    GPIO.cleanup()  # Cleans up GPIO
