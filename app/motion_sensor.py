import RPi.GPIO as GPIO
import time

from datetime import datetime

global message
import requests
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(5, GPIO.OUT)         #LED output pin

myMQTTClient = AWSIoTMQTTClient("ClientID")
myMQTTClient.configureEndpoint("account-specific-prefix.iot.aws-region.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi/certs/RasRootCA1.pem", "/home/pi/certs/RasPrivate.pem.key", "/home/pi/certs/Rasdevice.pem.crt")
 
Myvar= myMQTTClient.connect()

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print (f"Timestamp:{date}")

while True:
    i=GPIO.input(17)
    if i==0:                 #When output from motion sensor is LOW
        print("No intruders",i)
        GPIO.output(3, 0)  #Turn OFF LED
        message= "Intruder Detected"
        myMQTTClient.publish("topic/pi", "{\"MessageSent\":\""+ message + "\", \"Timestamp\" :\""+ str(date)+ "\"}", 0)
        time.sleep(1)
    elif i==1:               #When output from motion sensor is HIGH
        print("Intruder detected",i)
        GPIO.output(3, 1)  #Turn ON LED
        message= "No Intruder"
        myMQTTClient.publish("topic/pi", "{\"MessageSent\":\""+ message + "\", \"Timestamp\" :\""+ str(date)+ "\"}", 0)
        time.sleep(1)
