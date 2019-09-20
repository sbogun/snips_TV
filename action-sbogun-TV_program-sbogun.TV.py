#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
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
    


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("sbogun:TV_program", subscribe_intent_callback) \
         .start()
