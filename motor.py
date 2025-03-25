import RPi.GPIO as GPIO
import time

# GPIO Pin Setup
PWMA = 27  # Motor speed control (PWM)
AIN1 = 22  # Direction 1
AIN2 = 23  # Direction 2
STBY = 17  # Standby (must be HIGH to enable motors)

# GPIO Mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

# Enable Motor Driver (STBY HIGH)
GPIO.output(STBY, GPIO.HIGH)

# Set Direction (Forward)
GPIO.output(AIN1, GPIO.HIGH)
GPIO.output(AIN2, GPIO.LOW)

# Set Up PWM for Speed Control
pwm = GPIO.PWM(PWMA, 1000)  # 1kHz PWM frequency
pwm.start(0)  # Start with 0% duty cycle

try:
    while True:
        for speed in range(0, 101, 10):  # Increase speed from 0% to 100%
            pwm.ChangeDutyCycle(speed)
            print(f"Speed: {speed}%")
            time.sleep(1)
        
        for speed in range(100, -1, -10):  # Decrease speed back to 0%
            pwm.ChangeDutyCycle(speed)
            print(f"Speed: {speed}%")
            time.sleep(1)

except KeyboardInterrupt:
    print("Stopping motor.")
    pwm.stop()
    GPIO.cleanup()
