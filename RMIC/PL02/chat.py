# MQTT chat with rooms, paho-mqtt 2.1.0
# Usage: python chat.py <name> [broker]
# Commands: /join <room>  /rooms  /msg <name> <text>  /quit
# Rooms are topics srsa/chat/<room>, private messages go to srsa/dm/<name>.

import os
import sys
import paho.mqtt.client as mqtt

MQTT_BROKER = sys.argv[2] if len(sys.argv) > 2 else "10.6.1.61"
MQTT_PORT = 1883
PREFIX = "srsa"
NAME = sys.argv[1] if len(sys.argv) > 1 else input("Name: ")

room = "general"
seen_rooms = {room}

def valid(name):
    # MQTT wildcards and separators would break the topic
    return name and not any(c in name for c in "/+# ")

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        # ponytail: subscribe to every room so /rooms can list them, only the current one is printed
        client.subscribe(f"{PREFIX}/chat/#")
        client.subscribe(f"{PREFIX}/dm/{NAME}")
        client.publish(f"{PREFIX}/chat/{room}", f"* {NAME} joined")
        print(f"Connected to {MQTT_BROKER} as {NAME}, in #{room}. Commands: /join /rooms /msg /quit")
    else:
        print("Failed to connect:", reason_code)

def on_message(client, userdata, msg):
    text = msg.payload.decode(errors="replace")
    parts = msg.topic.split("/")
    if parts[1] == "dm":
        print(f"(private) {text}")
        return
    msg_room = parts[2]
    seen_rooms.add(msg_room)
    if msg_room == room:
        print(f"#{room} {text}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
if os.environ.get("MQTT_USER"):
    client.username_pw_set(os.environ["MQTT_USER"], os.environ.get("MQTT_PASS"))
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()  # network runs in background thread, main thread reads input

try:
    while True:
        text = input().strip()
        if not text:
            continue
        cmd, _, arg = text.partition(" ")
        if cmd == "/join":
            if not valid(arg):
                print("Usage: /join <room> (no spaces, / + #)")
                continue
            client.publish(f"{PREFIX}/chat/{room}", f"* {NAME} left")
            room = arg
            seen_rooms.add(room)
            client.publish(f"{PREFIX}/chat/{room}", f"* {NAME} joined")
        elif cmd == "/rooms":
            # ponytail: only rooms with activity since you connected, add retained room list if you need all
            print("Rooms:", ", ".join(f"#{r}" for r in sorted(seen_rooms)))
        elif cmd == "/msg":
            to, _, body = arg.partition(" ")
            if not valid(to) or not body:
                print("Usage: /msg <name> <text>")
                continue
            client.publish(f"{PREFIX}/dm/{to}", f"[{NAME}] {body}")
            print(f"(to {to}) {body}")
        elif cmd == "/quit":
            break
        else:
            client.publish(f"{PREFIX}/chat/{room}", f"[{NAME}] {text}")
except (KeyboardInterrupt, EOFError):
    pass
finally:
    client.publish(f"{PREFIX}/chat/{room}", f"* {NAME} left").wait_for_publish(2)
    print("\nBye")
    client.loop_stop()
    client.disconnect()
