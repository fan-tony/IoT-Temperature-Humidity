"""
Tony Fan
##Program that works with DHT22 temp sensor using breakout board and raspberry pi3
June 5/2019
"""
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)#using breakout board pins
GPIO.setwarnings(False)

pin = 26;#GPIO pin that the temperature sensor is set to
GPIO.setup(pin, GPIO.IN)#the temperature sensor is an input
sensor = Adafruit_DHT.DHT22;#sensor has properties of DHT22, as taken from adafruit library

#The main program
def loop():
    while True:#Makes sure that the program is always running
        humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
        print("Humidity is: " + str(humidity) + "     Temperature is: " + str(temperature));
        time.sleep(1)#needs 1 second delay between readings

    
if __name__ == '__main__':     #  Program start from here
    
    try:
            loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the function end() is executed
            end()
