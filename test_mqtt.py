#!/usr/bin/env python

import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish("paho/temperature", "temperature")

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set("/home/shubhamprash/Downloads/ca-cert.pem",
               None,
               None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
# disables peer verification
client.tls_insecure_set(True)
client.connect("192.168.0.6", 8883, 60)

client.loop_forever()
