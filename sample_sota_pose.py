import client_io
import json
import os
import time

ip = '192.168.11.x'
port = 22223
client = client_io.MyClient()
client.conect(ip, port)

data = {'msec': 2000, 'map': {'BODY_Y': 45}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
msec = client.read()
time.sleep(int(msec) / 1000)

data = {'msec': 2000, 'map': {'L_SHOU': 0}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
msec = client.read()
time.sleep(int(msec) / 1000)

data = {'msec': 2000, 'map': {'BODY_Y': 0, 'L_SHOU':  -90}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
msec = client.read()
time.sleep(int(msec) / 1000)

client.close()
