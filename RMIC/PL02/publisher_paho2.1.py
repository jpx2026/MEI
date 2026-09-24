# tested on Python 3.9.6, with Mosquitto 2.0.11
# uses paho-mqtt-2.1.0 (the sintax is different from paho-mqtt-1.x.x)
# MQTT Publisher

import paho.mqtt.publish as mqtt_publish
import time

MQTT_BROKER = "10.6.1.9"
MQTT_TOPIC = "srsa/topic1"

try:
    while True:
        mqtt_publish.single(MQTT_TOPIC, "Hello World!", hostname=MQTT_BROKER) #send data continuously every 3 seconds
        time.sleep(3)
except KeyboardInterrupt:
    print("Exiting publisher")