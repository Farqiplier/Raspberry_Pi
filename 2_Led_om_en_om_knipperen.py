from time import sleep
from gpiozero import LED
varLed1 = LED(18)
varLed2 = LED(6)
while True:

    varLed1.on()
    varLed2.off()
    sleep(1)
    varLed1.off()
    varLed2.on()
    sleep(1)