from sense_hat import SenseHat

sense = SenseHat() # This clears any pixels left on the Sense HAT. You may not need this step and may want to choose when to add it in.

sense.clear()
sense.set_pixel(0, 0, 255, 0, 0)
sense.set_pixel(0, 7, 0, 255, 0)
sense.set_pixel(7, 0, 0, 0, 255)
sense.set_pixel(7, 7, 255, 0, 255)
