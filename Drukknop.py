import gpiozero as io
from time import sleep

knop = io.Button(4, pull_up=False)

while True:
    sleep(0.1)
    if knop.value:
        print("Button is ingedrukt")
    else:
        print("Button is in rust")