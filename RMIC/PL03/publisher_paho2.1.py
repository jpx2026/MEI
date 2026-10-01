# tested on Python 3.9.6, with Mosquitto 2.0.11
# uses paho-mqtt-2.1.0 (the sintax is different from paho-mqtt-1.x.x)
# MQTT Publisher

import json
import paho.mqtt.client as mqtt
import random
import time

MQTT_BROKER = "10.6.1.67"
MQTT_PORT = 1883
MQTT_TOPIC = "home/temperature"

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="temperature_publisher",
)
client.will_set(MQTT_TOPIC, json.dumps(-1), qos=0, retain=True)
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

while True:
    temperature = round(random.uniform(15.0, 30.0), 1)
    payload = json.dumps({"sensor": "temperature", "value": temperature})
    client.publish(MQTT_TOPIC, payload, qos=0, retain=True)
    time.sleep(random.randint(1, 5))