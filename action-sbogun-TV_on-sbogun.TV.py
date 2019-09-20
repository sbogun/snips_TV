#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes, MqttOptions
import paho.mqtt.client as mqtt 
import json


MQTT_TOPIC = 'cmnd/sonoff/IRSend'
MQTT_MSG = json.dumps({"Protocol": "NEC", "Bits": 32, "Data": "0x616E02FD"});
MQTT_BROKER_ADDRESS = 'localhost:1883'



def subscribe_intent_callback(hermes, intent_message):
    intentname = intent_message.intent.intent_name

    if intentname == "sbogun:TV_on":
        mqttc = mqtt.Client() 
        mqttc.connect('localhost', 1883)
        mqttc.publish(MQTT_TOPIC, payload = MQTT_MSG)
        mqttc.disconnect()



if __name__ == "__main__":
    mqtt_opts = MqttOptions(broker_address=MQTT_BROKER_ADDRESS)
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intents(subscribe_intent_callback).start()
