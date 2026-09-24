import paho.mqtt.publish as publish
 
MQTT_BROKER = "10.6.1.9"
MQTT_TOPIC = "srsa"
import time
while True:
    publish.single(MQTT_TOPIC, "Hello World!", hostname=MQTT_BROKER) #send data continuously every 3 seconds
    time.sleep(3) 