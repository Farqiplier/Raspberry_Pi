import gpiozero as io
from time import sleep
from gpiozero import LED

varLed = LED(18)
knop = io.Button(4, pull_up=False)
time_passed = 0
hz = 0.1
while True:
    if knop.is_pressed:
        time_passed += hz
        sleep(hz)
        if time_passed >= 2:
            varLed.on()

    else:
        time_passed = 0
        varLed.off()
