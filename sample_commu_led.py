import client_io
import json
import os
import time

ip = '192.168.11.x'
port = 22224
client = client_io.MyClient()
client.conect(ip, port)

data = {'msec': 2000, 'map': {'BODY_G': 255}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
msec = client.read()
time.sleep(int(msec) / 1000)

client.close()