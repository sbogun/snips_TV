#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes, MqttOptions
import paho.mqtt.client as mqtt 
import json


MQTT_TOPIC = 'cmnd/sonoff/IRSend'
MQTT_BROKER_ADDRESS = 'localhost:1883'

MQTT_MSG = {}
MQTT_MSG['power_on_AMP'] = json.dumps({"Protocol": "NEC", "Bits": 32, "Data": "0x616E02FD"})
MQTT_MSG['0'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E08877"})
MQTT_MSG['1'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E020DF"})
MQTT_MSG['2'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E0A05F"})
MQTT_MSG['3'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E0609F"})
MQTT_MSG['4'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E010EF"})
MQTT_MSG['5'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E0906F"})
MQTT_MSG['6'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E050AF"})
MQTT_MSG['7'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E030CF"})
MQTT_MSG['8'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E0B04F"})
MQTT_MSG['9'] = json.dumps({"Protocol":"SAMSUNG","Bits":32,"Data":"0xE0E0708F"})

PROGRAM_KEY_MAP = {}
PROGRAM_KEY_MAP['daserste'] = [1]
PROGRAM_KEY_MAP['zdf'] = [2]
PROGRAM_KEY_MAP['arte'] = [3]
PROGRAM_KEY_MAP['sat1'] = [4]
PROGRAM_KEY_MAP['rtl'] = [5]
PROGRAM_KEY_MAP['rtl2'] = [6]
PROGRAM_KEY_MAP['pro7'] = [7]
PROGRAM_KEY_MAP['vox'] = [8]
PROGRAM_KEY_MAP['sixx'] = [9]
PROGRAM_KEY_MAP['tele5'] = [1,0]
PROGRAM_KEY_MAP['kabel1'] = [1,1]
PROGRAM_KEY_MAP['servustv'] = [1,2]
PROGRAM_KEY_MAP['pro7maxx'] = [1,3]
PROGRAM_KEY_MAP['one'] = [1,4]
PROGRAM_KEY_MAP['superrtl'] = [1,5]
PROGRAM_KEY_MAP['nitro'] = [1,6]
PROGRAM_KEY_MAP['sat1gold'] = [1,7]
PROGRAM_KEY_MAP['rtlplus'] = [1,8]
PROGRAM_KEY_MAP['rbb'] = [1,9]
PROGRAM_KEY_MAP['ndr'] = [2,0]
PROGRAM_KEY_MAP['hrfernsehen'] = [2,1]
PROGRAM_KEY_MAP['eurosport1'] = [3,6]
PROGRAM_KEY_MAP['ntv'] = [4,1]
PROGRAM_KEY_MAP['radio1'] = [6,5]
PROGRAM_KEY_MAP['cosmo'] = [1,0,7]
PROGRAM_KEY_MAP['jamfm'] = [1,2,0]
PROGRAM_KEY_MAP['fluxfm'] = [1,2,1]
PROGRAM_KEY_MAP['paradiso'] = [1,2,2]



def subscribe_intent_callback(hermes, intent_message):
    intentname = intent_message.intent.intent_name

    if intentname == "sbogun:TV_on":
        mqttc = mqtt.Client() 
        mqttc.connect('localhost', 1883)
        mqttc.publish(MQTT_TOPIC, payload = MQTT_MSG)
        mqttc.disconnect()

    elif intentname == "sbogun:TV_program":
        station_name = intent_message.slots.station_name.first()



if __name__ == "__main__":
    mqtt_opts = MqttOptions(broker_address=MQTT_BROKER_ADDRESS)
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intents(subscribe_intent_callback).start()
