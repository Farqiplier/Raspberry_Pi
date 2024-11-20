import gpiozero as io
from time import sleep
import random
speler1 = io.Button(21, pull_up=False)
speler2 = io.Button(20, pull_up=False)
StartKnop = io.Button(16, pull_up=False)

LED_speler1 = io.LED(19)
LED_speler2 = io.LED(26)

speler1WIN = False
speler2WIN = False
Start = False

teller1 = 0
teller2 = 0
tellerStart = 0
while True:
    LED_speler1.off()
    LED_speler2.off()
    StartStatus = StartKnop.is_pressed
    if StartStatus and not VorigeStartStatus:
        tellerStart += 1
    VorigeStartStatus = StartStatus
    if tellerStart %2 == 1:
        LED_speler1.on()
        LED_speler2.on()
        print("Game is begonnen")
        sleep(random.randint(2, 10))
        print("START")
        Start = True
    else:
        Start = False                                                                                                                                        


    while Start:


        StartStatus = StartKnop.is_pressed
        if StartStatus and not VorigeStartStatus:
            tellerStart += 1
        VorigeStartStatus = StartStatus
        if tellerStart %2 == 1:
            Start = True
        else:
            speler1WIN = False
            speler2WIN = False
            teller1 = 0
            teller2 = 0
            Start = False

        Speler1Status = speler1.is_pressed
        if Speler1Status and not (VorigeSpeler1Status or speler2WIN):
            teller1 += 1
        VorigeSpeler1Status = Speler1Status

        Speler2Status = speler2.is_pressed
        if Speler2Status and not (VorigeSpeler2Status or speler1WIN):
            teller2 += 1
        VorigeSpeler2Status = Speler2Status


        if teller1 %2 == 1 and speler1WIN == False:
            speler1WIN = True
            print("Speler 1 wint!")
            LED_speler2.off()

        
        if teller2 %2 == 1 and speler2WIN == False:
            speler2WIN = True
            print("speler 2 wint!")
            LED_speler1.off()