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

pin = 26;#temp sensor 
GPIO.setup(pin, GPIO.OUT)#the button pin is an output
tempS = Adafruit_DHT.DHT22;

#The main program
def loop():
    while True:#Makes sure that the program is always running
        humidity,temperature = Adafruit_DHT.read_retry(tempS,pin)
        print("Humidity is: " + str(humidity) + "     Temperature is: " + str(temperature));
        time.sleep(1)

    
if __name__ == '__main__':     #  Program start from here
    
    try:
            loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the function end() is executed
            end()
