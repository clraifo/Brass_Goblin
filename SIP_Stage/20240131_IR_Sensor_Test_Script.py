import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
ir_sensor_pin = 17  # Change this based on the GPIO pin you connected to the IR sensor
GPIO.setup(ir_sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(ir_sensor_pin):
            print("No object detected")
        else:
            print("Object detected!")
        time.sleep(1)  # Adjust this for faster or slower detection rate

except KeyboardInterrupt:
    print("Program terminated")

finally:
    GPIO.cleanup()
'''
Hardware Setup:
IR Sensor to Raspberry Pi Connection:

VCC of IR Sensor to 5V pin on Raspberry Pi (Pin 2 or 4).
GND of IR Sensor to Ground pin on Raspberry Pi (Pin 6, 9, 14, 20, or 25).
OUT of IR Sensor to a GPIO pin on Raspberry Pi (e.g., GPIO17, Pin 11).
Components:

Raspberry Pi.
Infrared (IR) sensor module.
Jumper wires.

Implementation Instructions:
Circuit Setup:

Connect your IR sensor to the Raspberry Pi following the hardware setup instructions above.
Create the Script:

Open the terminal on your Raspberry Pi.
Use nano ir_sensor_test.py to create a new file and enter the script provided.
Save and exit nano by pressing Ctrl+X, then Y to confirm changes, and Enter to exit.
Run the Script:

In the terminal, navigate to the directory where your script is saved.
Run the script by typing python3 ir_sensor_test.py and press Enter.
The script will print "Object detected!" when the IR sensor detects an object and "No object
detected" when there is no object in front of the sensor.
Testing:

Test the functionality by placing an object in front of the IR sensor and removing it. The 
messages printed to the console should change based on the presence of an object.

Notes:
------------------
** Ensure your IR sensor is powered correctly, and the OUT pin is connected to the correct 
GPIO pin on your Raspberry Pi.

** The time.sleep(1) command controls how frequently the script checks the sensor's state. Adjust this value as needed for your application.

** This script runs in an infinite loop until you manually stop it with a KeyboardInterrupt by pressing Ctrl+C in the terminal.

** This simple setup and script will help you verify that your IR sensor is working correctly with your Raspberry Pi, forming a foundation for more complex applications, such as triggering actions when an object is detected.


'''
