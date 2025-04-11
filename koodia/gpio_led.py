from gpiozero import LED, Button, Buzzer
from time import sleep

buzzer = Buzzer(5)
led = LED(17)
button = Button(4)

button.when_pressed = led.on
button.when_released = led.off

pause()
