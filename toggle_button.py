import gpiozero as io
from time import sleep
from gpiozero import LED

varLed = LED(18)
knop = io.Button(4, pull_up=False)
press_counter = 0
while True:
    if knop.is_pressed:
        press_counter += 1
        sleep(1)
    if press_counter % 2 == 0:
        varLed.off()
    else:
        varLed.on()
