from time import sleep
from gpiozero import LED
varLed = LED(18)
while True:

    varLed.on()
    sleep(1)
    varLed.off()
    sleep(1)