import time 
from w1thermsensor import W1ThermSensor
import adafruit_dht
import board
from gpiozero import LED


RodeLed = LED(18)
sensor = W1ThermSensor()
dhtDevice = adafruit_dht.DHT11(board.D17)
f = open("Waardes.txt", "a")
varX = time.ctime()

#Als het verschil in temperatuur meer is dan 5°C gaat er een rode led branden. Op dat moment komt er in het tekstbestand de tekst "temperatuurverschil te hoog, check de sensoren" te staan
while True: 
    time.sleep(3)
    
    shieldtemperatuur = round(sensor.get_temperature())
    dhttemperature = round(dhtDevice.temperature)
    
    print(f"De temperatuur gemeten door de DHT11 is nu {dhttemperature}°C")
    print(f"De temperatuur gemeten door de shield is nu {shieldtemperatuur}°C")
    print(f"De gemiddelde temperatuur is nu {(shieldtemperatuur + dhttemperature) / 2}°C")
    print("---------------------------------------")
    
    f.write(f"De gemiddelde temperatuur is nu {(shieldtemperatuur + dhttemperature) / 2}\n")
    if abs((shieldtemperatuur - dhttemperature)) > 5:
        RodeLed.on()
        f.write("Temperatuurverschil te hood, check de sensoren.\n")
    else:
        RodeLed.off()
    f.write(f"De tijd is nu {varX}\n")
    f.write("---------------------------------------\n")
    f.close()

