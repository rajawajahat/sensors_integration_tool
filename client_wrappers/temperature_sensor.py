import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 16
instance = dht11.DHT11(pin = 16)
result = instance.read()

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else:
    print("not valid")
    print("Error: %d" % result.error_code)
