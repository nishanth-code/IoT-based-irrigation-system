import time
import ubinascii
from umqtt.simple import MQTTClient
import machine
import sample as waterP



# Adafruit IO MQTT broker settings
ADAFRUIT_IO_URL = "io.adafruit.com"
ADAFRUIT_IO_USERNAME = "nish3456"
ADAFRUIT_IO_KEY = "aio_FRlF39hmb2v9GNqF1tWrKEEfkESN"
ADAFRUIT_IO_TOPIC = "nish3456/feeds/temperature"

# Generate a unique MQTT client ID
CLIENT_ID = ubinascii.hexlify(machine.unique_id())

# Callback function for received messages
def callback(topic, message):
    print("Received message on topic: {}, message: {}".format(topic, message))
def sub_cb(topic, msg):
    action=msg.decode()
    print(action)
    if action == 'ON':
        waterP.waterpump_on()
        
    else:
        waterP.waterpump_off()
        
        



def publish(temperature,humidity,condition,soilMD,soilMA):
    
    mqtt_client = MQTTClient(CLIENT_ID, ADAFRUIT_IO_URL, user=ADAFRUIT_IO_USERNAME, password=ADAFRUIT_IO_KEY)
    mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    
    mqtt_client.publish(ADAFRUIT_IO_TOPIC,str(temperature))
    mqtt_client.publish("nish3456/feeds/humidity",str(humidity))
    mqtt_client.publish("nish3456/feeds/feels like",condition)
    mqtt_client.publish("nish3456/feeds/soilmd",str(soilMD))
    mqtt_client.publish("nish3456/feeds/soilma",str(soilMA))
    
    
def subscribe():
    mqtt_client = MQTTClient(CLIENT_ID, ADAFRUIT_IO_URL, user=ADAFRUIT_IO_USERNAME, password=ADAFRUIT_IO_KEY)
    mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    mqtt_client.subscribe("nish3456/feeds/pumpState")
    while True:
        mqtt_client.wait_msg()
        
        
    
        
    
        # Additional code for your application logic here
        # ...
        



