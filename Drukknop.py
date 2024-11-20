import gpiozero as io
from time import sleep

knop = io.Button(21, pull_up=False)

while True:
    sleep(0.1)
    currentState = knop.is_pressed
    if currentState and not previousState:
        print("Button is ingedrukt")
    else:
        print("Button is in rust")                                                                                                                                               
    previousState = currentState
    sleep(0.1)