#!/usr/bin/python
# -*- coding: latin-1 -*-
#Python ei tykkää ääkkösistä kommenteissa
import os, sys
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

red = (255, 0, 0)
green = (0, 255, 0)

while True:
	#Otetaan sensoreiden arvot
	p = sense.get_pressure()
	t = sense.get_temperature()
	h = sense.get_humidity()
	
	#Pyöristetään arvot
	t = round(t, 1)
	p = round(p, 1)
	h = round(h, 1)
	
	message = "Lampotila: " + str(t) + " Ilmanpaine: " + str(p) + " Kosteus: " + str(h)
	print(t, p, h )
	
	if t > 18.3 and t < 26.7:
		bg = green
	else:
		bg = red
	
	sense.show_message(message, scroll_speed=0.1, back_colour=bg)
