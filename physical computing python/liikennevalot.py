from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(4)
lights = TrafficLights(24, 23, 22)
buzzer = Buzzer(18)

while True:
	button.wait_for_press()
	sleep(10)
	buzzer.off()
	lights.off()
	lights.red.on()
	sleep(10)
	button.wait_for_release()
	lights.off()
	lights.green.on()
	buzzer.on()
	sleep(10)
	lights.amber.on()
	lights.green.off()
	buzzer.off()
	sleep(1)
	lights.red.on()
	lights.amber.off()
	sleep(10)
	lights.amber.on()
	sleep(1)
	lights.off()
	lights.green.on()
	buzzer.on()
	sleep(10)
#	lights.off() nämä on tässä vain testausta varten
#	buzzer.off()
