# IoTMotionDetect
# Creating IoT motion sensor and publish to AWS IoT

This project is to demonstrate the IoT device/endpoint to detect the motion object using Raspberry, PIR motion sensor and Led and then publish the message to cloud platform using AWS IoT. The Python Software is used to program in the project
# 1.	IoT endpoint device with Raspberry
Hardware connection:
Typically, the PIR motion sensor and led will connect with Raspberry Pi through pins in GPIO connector. The figure below shows the 40 I/O pins in the GPIO header on the Raspberry. Noted that there are two methods to assign the I/O pins: using GPIO pin number or actual pin number on the board. 
  
To test the circuit, you can create the simple circuit to read the output data from a PIR motion sensor and write a simple code to turn the led on as the following figure and source.
 
Source: https://gpiozero.readthedocs.io/en/stable/recipes.html
# 2.	Connect IoT endpoint (Raspberry to AWS IoT core)
AWS IoT provides instruction to connect your IoT endpoint to AWS so you can use the cloud services for your application. There are four supporting protocols from AWS IoT:
•	MQTT (Message Queuing and Telemetry Transport)
•	MQTT over WSS (Websockets Secure)
•	HTTPS (Hypertext Transfer Protocol - Secure) 
•	LoRaWAN (Long Range Wide Area Network)eht nIn this example, we will need to install AWS IoT Device SDK for Python v2 on GitHub in Raspberry, create the program to connect the raspberry to AWS IoT using MQTT protocol. The instruction to install AWS IOT SDK can be found at link https://github.com/aws/aws-iot-device-sdk-python-v2 and the simple python program in the folder.

# 3.	Store your date to S3 
In this project, the captured data will be sent from aws IoT to S3 using AWS Kinesis Firehorse. It is the easiest way to reliably load streaming data into data lakes (S3), data stores, and analytics services. The data can capture, transform, and load to S3 in near real time. As a result, you can later access new data in S3 and react to business and operational events faster.
 
The link below shows how to create a Kinesis Data Firehose delivery stream to S3.
https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html

# 4.	Creating rule to query data and send to S3 through kinesis Firehorse
You configure rules to route data from your IoT endpoint. You will go to console > AWS IoT>Act>Rules> create the rules. Alternative, you can find the method to create rules in this link:
https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html
 
# 5.	Open file in S3

