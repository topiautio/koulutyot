from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

B = (102, 51, 0)
b = (0, 0, 255)
S = (205,133,63)
W = (255, 255, 255)
g = (0, 255, 0) 
m = (0, 0, 0) 

while True:
	steve_pixels = [
		B, B, B, B, B, B, B, B,
		B, B, B, B, B, B, B, B,
		B, S, S, S, S, S, S, B,
		S, S, S, S, S, S, S, S,
		S, W, b, S, S, b, W, S,
		S, S, S, B, B, S, S, S,
		S, S, B, S, S, B, S, S,
		S, S, B, B, B, B, S, S
	]

	sense.set_pixels(steve_pixels)
	sleep(5)



	creeper_pixels = [
		g, g, g, g, g, g, g, g,
		g, g, g, g, g, g, g, g,
		g, m, m, g, g, m, m, g,
		g, m, m, g, g, m, m, g,
		g, g, g, m, m, g, g, g,
		g, g, m, m, m, m, g, g,
		g, g, m, m, m, m, g, g,
		g, g, m, g, g, m, g, g
	]

	sense.set_pixels(creeper_pixels)
	sleep(5)
