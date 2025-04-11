from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

while True:
    sense.show_message("Paljon tekstia", text_colour=red, back_colour=black, scroll_speed=0.1)
