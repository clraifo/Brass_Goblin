import time
import picamera

# Number of images to capture
num_images = 100

# Delay between images in seconds
delay = 3  # 3 seconds

# Initialize the camera
with picamera.PiCamera() as camera:
    # Set camera resolution (optional, change as needed)
    camera.resolution = (1024, 768)

    for i in range(num_images):
        try:
            # Construct filename based on the iteration
            filename = f"image_{i:04d}.jpg"

            # Capture the image
            camera.capture(filename)

            # Print status message
            print(f"Captured {filename}")

            # Wait for a few seconds
            time.sleep(delay)

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop in case of an error

print("Image capture complete.")

'''
### Equipment Needed:
1. Raspberry Pi 4B: Your main computer board
2. Raspberry Pi Camera Module 2: The camera that will capture images
3. MicroSD Card: For the Raspberry Pi operating system and storage
4. Power Supply: For the Raspberry Pi
5. Monitor, Keyboard, and Mouse: For initial setup (these can be removed later if you access the Raspberry Pi remotely)

### Wiring and Setup:
1. Setting Up the Raspberry Pi*:
   - Insert the MicroSD card with the Raspberry Pi OS installed into your Raspberry Pi
   - Connect the Raspberry Pi to a monitor, keyboard, and mouse
   - Plug in the power supply to boot up the Raspberry Pi

2. Connecting the Camera Module:
   - First, power down your Raspberry Pi (shut down from the OS and unplug the power supply)
   - Locate the camera port (CSI port) on the Raspberry Pi. It's a flat, narrow port, usually between the HDMI and audio jack
   - Gently lift the plastic clip on the CSI port
   - Insert the ribbon cable from the Camera Module into the CSI port, with the silver contacts facing away from the 
     Ethernet port (towards the HDMI ports)
   - Gently press the plastic clip back down to secure the ribbon cable
   - Mount the Camera Module in your desired location

3. Software Configuration:
   - Power up the Raspberry Pi
   - Open the Raspberry Pi Configuration tool from the Preferences menu
   - In the Interfaces tab, enable the camera and reboot the Raspberry Pi if prompted

4. Testing the Camera:
   - After reboot, open a terminal and try a simple command like `raspistill -o test.jpg` to test if the camera captures 
     a photo

### Additional Notes:
- The Raspberry Pi Camera Module 2 connects directly to the Raspberry Pi via the CSI port. No breadboard or jumper wires 
  are required for this connection
- Ensure that your Pi's power supply is adequate (5V/3A for a Raspberry Pi 4B)
- If you plan to access your Raspberry Pi remotely, you can set up SSH and/or VNC for headless operation
- Be sure to handle the camera module and the ribbon cable gently to avoid damage

This setup is primarily for capturing images using the Raspberry Pi Camera Module 2. If you plan to expand the project with 
additional sensors or components, the breadboard and jumper wires will become more relevant. For now, your setup should 
be simple and focused on the camera functionality.
'''
