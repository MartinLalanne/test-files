from paho.mqtt import client as mqtt
import time
import ssl
import calendar
import datetime
import json
import random

def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed for m' + str(mid))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))

def on_log(client, userdata, level, buf):
    print("log: ",buf)

device_id = "" # Add device id
iot_hub_name = "" # Add iot hub name
sas_token = "" # Add sas token string
client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311,  clean_session=False)
client.on_log = on_log
client.tls_set_context(context=None)

# Set up client credentials
username = "{}.azure-devices.net/{}/api-version=2018-06-30".format(iot_hub_name, device_id)
client.username_pw_set(username=username, password=sas_token)

# Connect to the Azure IoT Hub
client.on_connect = on_connect
client.connect(iot_hub_name+".azure-devices.net", port=8883)

# Publish
time.sleep(1)
for x in range(3):        
        exp = datetime.datetime.utcnow() 
        abcstring1={
                "AI01":random.randint(0, 100)
        }
        data_out1 = json.dumps(abcstring1)
        client.publish("devices/{device_id}/messages/events/".format(device_id=device_id), payload=data_out1, qos=1, retain=False)
        print("Publishing on devices/" + device_id + "/messages/events/",data_out1)
        time.sleep(5)

# Subscribe 
client.on_message = on_message
client.on_subscribe = on_subscribe 
client.subscribe("devices/{device_id}/messages/devicebound/#".format(device_id=device_id))

client.loop_forever() 