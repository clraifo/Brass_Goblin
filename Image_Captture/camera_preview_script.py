from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)  # Adjust the duration for how long you want the preview to stay on
camera.stop_preview()
