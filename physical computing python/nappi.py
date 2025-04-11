from gpiozero import Button, LED
from time import sleep
led = LED(24)
button = Button(4)
while True:
	button.wait_for_press()
	led.on()
	sleep(3)
	led.off()
