# MQTT publisher for humidity; tested with paho-mqtt 2.1.0.

import json
import paho.mqtt.client as mqtt
import random
import time

MQTT_BROKER = "10.6.1.67"
MQTT_PORT = 1883
MQTT_TOPIC = "home/humidity"

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="humidity_publisher",
)
client.will_set(MQTT_TOPIC, json.dumps(-1), qos=0, retain=False)
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

while True:
    humidity = round(random.uniform(30.0, 70.0), 1)
    #humidity = "Diogo"
    payload = json.dumps({"sensor": "humidity", "value": humidity})
    client.publish(MQTT_TOPIC, payload, qos=0, retain=False)
    time.sleep(random.randint(1, 5))