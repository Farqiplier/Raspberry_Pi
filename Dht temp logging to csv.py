from time import sleep, strftime
import adafruit_dht
import board
Dht1 = adafruit_dht.DHT11(board.D17)
Dht2 = adafruit_dht.DHT11(board.D27)

with open("/home/rpi/Python/Github/Raspberry_Pi/Temp_log.csv", "a") as log:

    while True:
        sleep(3)
        try:
            temperature1 = Dht1.temperature
            temperature2 = Dht2.temperature
        except RuntimeError as error:
            print(error.args[0])
            continue
        print(f"Temp Dht1: {temperature1}C Temp Dht2: {temperature2}C ")
        log.write("{0}, Temp1: {1}, Temp2: {2}\n".format(strftime("Datum: %Y/%m/%d, Tijd: %H:%M:%S"), temperature1, temperature2))

