import gpiozero as io #Importeer de library om te gebruiken voor de knop
from time import sleep # importeer sleep functie van de time library
from gpiozero import LED # importeer Led functie van de gpiozero library
 
# Maak variabele voor alle Led's en de knop voor de voetgangers
rood_stoplicht = LED(26)
oranje_stoplicht = LED(19)
groen_stoplicht = LED(13)
rood_voetganger = LED(20)
groen_voetganger = LED(16)
 
knop = io.Button(4, pull_up=False)
 
pressed = False #variabele die true wordt als de knop wordt ingedrukt
delay = False # variabele voor de delay van een minuut nadat het voetgangerslicht terug rood wordt
 
while True:
    groen_stoplicht.on() # Zet het stoplicht op groen
    rood_voetganger.on() # Zet het voetgangerslicht op rood
    if delay == True: # Als de delay true is, 
        sleep(60) # wacht 1 minuut
        delay = False # Zet de delay op false
    if knop.is_pressed: # Als de knop wordt ingedrukt, 
        pressed = True # zet de variabele pressed op true
    else: # Als de knop niet wordt ingedrukt, zet de variabele pressed op false
        pressed = False # zet de variabele pressed op false
    if pressed == True and delay == False: # Als de knop wordt ingedrukt en de delay is false, 
        groen_stoplicht.off() # zet het stoplicht op rood
        oranje_stoplicht.on() # zet het oranje stoplicht aan
        sleep(2) # wacht 2 seconden
        oranje_stoplicht.off() # zet het oranje stoplicht uit
        rood_stoplicht.on() # zet het stoplicht op rood
        rood_voetganger.off() # zet het voetgangerslicht op groen
        groen_voetganger.on() # zet het voetgangerslicht op groen
        sleep(120) # wacht 2 minuten
        delay = True # zet de delay op true
        groen_voetganger.off() # zet het voetgangerslicht op rood
        rood_stoplicht.off() # zet het stoplicht op groen