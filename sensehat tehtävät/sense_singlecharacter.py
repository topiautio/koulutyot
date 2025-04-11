from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

sense.show_letter("F")

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

def random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

sense.show_letter("T", random_colour())
sleep(1)
sense.show_letter("e", random_colour())
sleep(1)
sense.show_letter("s", random_colour())
sleep(1)
sense.show_letter("t", random_colour())
sleep(1)
sense.show_letter("i", random_colour())
sleep(1)
sense.clear()
