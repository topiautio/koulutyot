from gpiozero import MCP3008, PWMLED

led = PWMLED(27)
pot = MCP3008(0)


#potentiometri ei toimi
while True:
	led.value = pot.value
