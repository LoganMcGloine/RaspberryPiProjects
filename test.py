from gpiozero import LED, Button, Buzzer, DistanceSensor
from time import sleep
import datetime
from signal import signal, SIGINT
import sys

led = LED(17)
button = Button(2)
buzzer = Buzzer(14)
#pir = MotionSensor(15)
ultrasonic = DistanceSensor(echo=15, trigger=18)

#while True:
#	print(ultrasonic.distance)

def signal_handler(sig, frame):
	print('\nExiting program')
	led.off()
	buzzer.off()
	sys.exit(0)

# Register the signal handler
signal(SIGINT, signal_handler)

# Initial buzzer beep
buzzer.on()
sleep(1)
buzzer.off()

print("Program running. Press Ctrl+C to exit")
while True:
#	pir.wait_for_motion()
	button.wait_for_press()
	led.on()
	buzzer.on()
	sleep(1)
	led.off()
	buzzer.off()
#	print("movement detected at ", datetime.datetime.now().strftime("%H:%M:%S"))

# Clean up GPIO pins
GPIO.cleanup()
