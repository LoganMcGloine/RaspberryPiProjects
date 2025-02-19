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
    
    # Setup PWM on enable pin with 100Hz frequency
    global pwm
    pwm = GPIO.PWM(ENABLE_PIN, 100)
    pwm.start(0)  # Start with 0% duty cycle

def motor_forward(speed=100):
    GPIO.output(CONTROL_1_PIN, GPIO.HIGH)
    GPIO.output(CONTROL_2_PIN, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def motor_backward(speed=100):
    GPIO.output(CONTROL_1_PIN, GPIO.LOW)
    GPIO.output(CONTROL_2_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)

def motor_stop():
    pwm.ChangeDutyCycle(0)
    GPIO.output(CONTROL_1_PIN, GPIO.LOW)
    GPIO.output(CONTROL_2_PIN, GPIO.LOW)

def cleanup():
    pwm.stop()
    GPIO.cleanup()

# Main execution
setup_motor()
try:
    # Accelerate from 0 to 100% over 2 seconds
    for speed in range(0, 101, 2):  # Increment by 2% each step
        motor_forward(speed)
        time.sleep(0.04)  # 2 seconds / 50 steps = 0.04 seconds per step
    
    # Run at full speed for 4 seconds
    time.sleep(4)
    
    motor_stop()
finally:
    cleanup()

