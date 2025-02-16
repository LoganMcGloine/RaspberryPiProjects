from gpiozero import LED, Button, Buzzer, MotionSensor, DistanceSensor
from time import sleep
import datetime
import keyboard


led = LED(17)
button = Button(2)
buzzer = Buzzer(14)
#pir = MotionSensor(15)
ultrasonic = DistanceSensor(echo=15, trigger=18)

#while True:
#	print(ultrasonic.distance)


led_on = False
buzzer.on()
sleep(1)
buzzer.off()
while True:
#	pir.wait_for_motion()
	button.wait_for_press()
	led.on()
	buzzer.on()
	sleep(1)
	led.off()
	buzzer.off()
#	print("movement detected at ", datetime.datetime.now().strftime("%H:%M:%S"))

	if keyboard.is_pressed('q'):
		break

# Clean up GPIO pins
GPIO.cleanup()
