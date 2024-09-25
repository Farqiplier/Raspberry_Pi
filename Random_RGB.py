from time import sleep
from gpiozero import LED
import random
RGBLedRood = LED(13)
RGBLedGroen = LED(19)
RGBLedBlauw = LED(26)

while True:
    rood = random.randint(0, 1)
    groen = random.randint(0, 1)
    blauw = random.randint(0, 1)

    RGBLedRood.on()
    RGBLedGroen.on()
    RGBLedBlauw.on()

    sleep(1)
    RGBLedRood.off()
    RGBLedGroen.off()
    RGBLedBlauw.off()

    sleep(1)