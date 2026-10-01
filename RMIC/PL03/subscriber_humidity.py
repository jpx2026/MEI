# MQTT subscriber for humidity; tested with paho-mqtt 2.1.0.

import paho.mqtt.client as mqtt_subscribe

MQTT_BROKER = "10.6.1.67"
MQTT_PORT = 1883
MQTT_TOPIC = "home/humidity"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC, qos=0)
    else:
        print(f"Failed to connect, return code {reason_code}")


def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}")


client = mqtt_subscribe.Client(
    callback_api_version=mqtt_subscribe.CallbackAPIVersion.VERSION2
)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Desconectar subscriber humidade")
finally:
    client.disconnect("A desconectar a humidade")