#tuodaan kaikki tarvittavat kirjastot. 
#LEDCharDisplay ja LEDMultiCharDisplay ovat tärkeimmät.
from itertools import cycle
from collections import deque
from gpiozero import LEDMultiCharDisplay, LEDCharDisplay
from signal import pause

#määritellään 7segment näyttö
#numerot 20-26 ovat kytkettynä segmentteihin A-D ja 27 on desimaali
#numerot 4 ja 5 ovat näytöt joita ohjataan
display = LEDMultiCharDisplay(
    LEDCharDisplay(20, 21, 22, 23, 24, 25, 26, dp=27), 4, 5)

#tehdään vierivä teksti
def scroller(message, chars=2):
    d = deque(maxlen=chars)
    for c in cycle(message):
        d.append(c)
        if len(d) == chars:
            yield ''.join(d)

#tekstin liikkumisnopeus ja teksti jota halutaan näyttää
#tietääkseni tässä voi käyttää vain isoja kirjaimia tai numeroita mutta ei erikoismerkkejä kuten "-" tai "."
display.source_delay = 0.2
display.source = scroller('ELEHTRONIIHHA ASENTAJA  ')
pause()
