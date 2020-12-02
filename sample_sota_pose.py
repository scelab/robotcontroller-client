import client_io
import json
import os
import time

ip = '192.168.0.60'
port = 22223

client = client_io.MyClient()
client.connect(ip, port)
data = {'msec': 2000, 'map': {'BODY_Y': 45}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
client.close()
time.sleep(int(data['msec']) / 1000)

client = client_io.MyClient()
client.connect(ip, port)
data = {'msec': 2000, 'map': {'L_SHOU': 0}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
client.close()
time.sleep(int(data['msec']) / 1000)

client = client_io.MyClient()
client.connect(ip, port)
data = {'msec': 2000, 'map': {'BODY_Y': 0, 'L_SHOU':  -90}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
client.close()
time.sleep(int(data['msec']) / 1000)

