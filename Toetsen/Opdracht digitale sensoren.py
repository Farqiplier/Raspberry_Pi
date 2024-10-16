# script_0603_temperatuursensor BS18B20
import time 
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True: 
    temperatuur = sensor.get_temperature()
    print("De temperatuur in graden Celcius is nu", round(temperatuur))
    time.sleep(1)