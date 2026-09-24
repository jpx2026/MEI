# tested on Python 3.9.6, with Mosquitto 2.0.11
# uses paho-mqtt-2.1.0 (the sintax is different from paho-mqtt-1.x.x)
# MQTT Subscriber

import paho.mqtt.client as mqtt_subscribe # import library
 
MQTT_BROKER = "10.6.1.9" # specify the broker address (e.g., IP of the Raspberry Pi, localhost)
MQTT_PORT = 1883    # broker port
MQTT_TOPIC = "srsa/topic1" # this is the name of topic, like temp

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    # For paho-mqtt 2.0.0+, you need to have the properties parameter
    if reason_code == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", reason_code)
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # subscribe topic
    client.subscribe(MQTT_TOPIC)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
 
# For paho-mqtt 2.0.0+, you need to set callback_api_version.
client = mqtt_subscribe.Client(callback_api_version=mqtt_subscribe.CallbackAPIVersion.VERSION2)

# set callback function on connecting
client.on_connect = on_connect

# set callback function on new message received
client.on_message = on_message

# Connect to MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT)

try:
    # use client.loop_forever() if you don't want to write any further code. It blocks the code forever to check for data
    # use client.loop_start() if you want to write any more code here
    client.loop_forever()
except KeyboardInterrupt:
    print("Exiting subscriber")
