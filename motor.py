import RPi.GPIO as GPIO
import time

# Define GPIO pins
ENABLE_PIN = 17
CONTROL_1_PIN = 27
CONTROL_2_PIN = 22

def setup_motor():
    # Set GPIO mode
    GPIO.setmode(GPIO.BCM)
    
    # Setup pins as outputs
    GPIO.setup(ENABLE_PIN, GPIO.OUT)
    GPIO.setup(CONTROL_1_PIN, GPIO.OUT)
    GPIO.setup(CONTROL_2_PIN, GPIO.OUT)

def motor_forward():
    GPIO.output(ENABLE_PIN, GPIO.HIGH)
    GPIO.output(CONTROL_1_PIN, GPIO.HIGH)
    GPIO.output(CONTROL_2_PIN, GPIO.LOW)

def motor_backward():
    GPIO.output(ENABLE_PIN, GPIO.HIGH)
    GPIO.output(CONTROL_1_PIN, GPIO.LOW)
    GPIO.output(CONTROL_2_PIN, GPIO.HIGH)

def motor_stop():
    GPIO.output(ENABLE_PIN, GPIO.LOW)
    GPIO.output(CONTROL_1_PIN, GPIO.LOW)
    GPIO.output(CONTROL_2_PIN, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

setup_motor()
try:
    motor_forward()
    time.sleep(2)  # Run forward for 2 seconds
    motor_backward()
    time.sleep(2)  # Run backward for 2 seconds
    motor_stop()
finally:
    cleanup()

