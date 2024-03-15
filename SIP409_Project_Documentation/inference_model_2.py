from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import numpy as np
from PIL import Image
from tflite_runtime.interpreter import Interpreter
import os

# GPIO pin setup
DIR_PIN = 16
STEP_PIN = 17
ENABLE_PIN = 23

# Stepper motor configuration
CW = 1
CCW = 0
STEPS = 19000

# Base directory for project
BASE_DIR = '/home/clraifo/BG/TFLite_LC_and_non_LC_20240310'

# TFLite model and labels
MODEL_PATH = os.path.join(BASE_DIR, 'model_unquant.tflite')
LABELS_PATH = os.path.join(BASE_DIR, 'labels.txt')

# Initialize camera
camera = PiCamera()
camera.resolution = (1024, 768)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.output(ENABLE_PIN, GPIO.LOW)

def load_labels(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def set_up_interpreter(model_path):
    interpreter = Interpreter(model_path)
    interpreter.allocate_tensors()
    return interpreter

def preprocess_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    image_array = np.expand_dims(np.array(image), axis=0)
    return image_array.astype(np.float32)

def classify_image(interpreter, image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return np.argmax(output_data)

def rotate_motor(direction, steps, delay=0.00005):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

def main():
    labels = load_labels(LABELS_PATH)
    interpreter = set_up_interpreter(MODEL_PATH)
    image_counter = 1  # Initialize image counter
    try:
        while True:
            # Define the path for each captured image
            image_path = os.path.join(BASE_DIR, 'Inference_images', f'captured_image_{image_counter:03d}.jpg')
            camera.capture(image_path)
            print(f"Image captured and saved to: {image_path}")
            image = preprocess_image(image_path)
            classification = classify_image(interpreter, image)
            label = labels[classification]
            print(f"Classification: {label}")

            if label == 'Lake City':
                rotate_motor(CW, STEPS)
                rotate_motor(CCW, STEPS)
            else:
                rotate_motor(CCW, STEPS)
                rotate_motor(CW, STEPS)

            image_counter += 1  # Increment image counter for next capture
            if input("Press Enter to continue or 'q' to quit: ").lower() == 'q':
                break

    finally:
        GPIO.output(ENABLE_PIN, GPIO.HIGH)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
