from time import sleep, strftime # Importeer sleep en strftime van de time module
import adafruit_dht # Importeer adafruit_dht
import board # Importeer board
import os # Importeer os
Dht1, Dht2 = adafruit_dht.DHT11(board.D17), adafruit_dht.DHT11(board.D27) # Maak twee variabele van de klasse DHT11 aan
file_path = os.path.join(os.path.dirname(__file__), "Temp_log.csv") # Maak een bestand aan met de naam Temp_log.csv in dezelfde locatie als dit bestand

with open(file_path, "a") as log: # Open het bestand in append mode
    log.write("Datum, Tijd, Temp1, Temp2, Gemiddelde\n") # Schrijf de header naar het bestand
    while True: # Start een oneindige loop
        sleep(2) # Wacht 2 seconden
        try: # Probeer de volgende code
            temperature1, temperature2 = Dht1.temperature, Dht2.temperature # Maak twee variabelen aan met de temperatuur van de twee sensoren
            gemiddelde_temp = round((temperature1 + temperature2) / 2) # Maak een variabele aan met het gemiddelde van de twee temperaturen
        except RuntimeError as error: # Als er een RuntimeError optreedt
            print(error.args[0]) # Print de error
            continue # Ga verder met de volgende iteratie van de loop
        log.write("{0}, {1}, {2}, {3}\n".format(strftime("%d/%m/%Y, %H:%M:%S"), temperature1, temperature2, gemiddelde_temp)) # Schrijf de datum, tijd, temperatuur van sensor 1, temperatuur van sensor 2 en het gemiddelde naar het bestand

