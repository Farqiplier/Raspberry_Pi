from time import sleep, strftime
import adafruit_dht
import board
Dht1, Dht2 = adafruit_dht.DHT11(board.D17), adafruit_dht.DHT11(board.D27)
with open("/home/rpi/Python/Github/Raspberry_Pi/Temp_log.csv", "a") as log:
    log.write("Datum, Tijd, Temp1, Temp2, Gemiddelde\n")
    while True:
        sleep(2)
        try:
            temperature1,temperature2, gemiddelde_temp  = Dht1.temperature, Dht2.temperature, round((temperature1 + temperature2) / 2)
        except RuntimeError as error:
            print(error.args[0])
            continue
        log.write("{0}, {1}, {2}, {3}\n".format(strftime("%Y/%m/%d, %H:%M:%S"), temperature1, temperature2, gemiddelde_temp))

