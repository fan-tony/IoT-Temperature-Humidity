from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import RPi.GPIO as GPIO
import time
import Adafruit_DHT


# A random programmatic shadow client ID.
SHADOW_CLIENT = "myShadowClient"

# The unique hostname that AWS IoT generated for 
# this device.
HOST_NAME = "a15eahaf2jb49q-ats.iot.us-east-2.amazonaws.com"

# The relative path to the correct root CA file for AWS IoT, 
# that you have already saved onto this device.
ROOT_CA = "AmazonRootCA1.pem"

# The relative path to your private key file that 
# AWS IoT generated for this device, that you 
# have already saved onto this device.
PRIVATE_KEY = "XXXXXXXXXX-private.pem.key"

# The relative path to your certificate file that 
# AWS IoT generated for this device, that you 
# have already saved onto this device.
CERT_FILE = "XXXXXXXXXX-certificate.pem.crt.txt"

# A programmatic shadow handler name prefix.
SHADOW_HANDLER = "MyRPi"

# Automatically called whenever the shadow is updated.
def myShadowUpdateCallback(payload, responseStatus, token):
  print()
  print('UPDATE: $aws/things/' + SHADOW_HANDLER +
    '/shadow/update/#')
  print("payload = " + payload)
  print("responseStatus = " + responseStatus)
  print("token = " + token)

# Create, configure, and connect a shadow client.
myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,
  CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()

# Create a programmatic representation of the shadow.
myDeviceShadow = myShadowClient.createShadowHandlerWithName(
  SHADOW_HANDLER, True)


GPIO.setmode(GPIO.BCM)#using breakout board pins
GPIO.setwarnings(False)

pin = 26;#digital pin of temp sensor
GPIO.setup(pin, GPIO.IN)#the temperature pin is an input pin
sensor = Adafruit_DHT.DHT22;#sensor is an object with DHT22 properties taken from adafruit library


while True:

    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)#read and store humidity and temperature

    myDeviceShadow.shadowUpdate(
    '{"state":{"reported":{"Temperature":' + str(temperature)+
    ', "Humidity":' + str(humidity)+'}}}',
    myShadowUpdateCallback, 5)

    # Wait for this test value to be added.
    time.sleep(5)
