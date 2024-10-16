import time
import adafruit_dht
import board
dhtDevice = adafruit_dht.DHT11(board.D17)

while True:
    
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature, humidity))
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(2.0)