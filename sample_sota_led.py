import client_io
import json
import os
import time

ip = '192.168.0.60'
port = 22224
client = client_io.MyClient()
client.conect(ip, port)

data = {'msec': 2000, 'map': {'L_EYE_R': 255, 'L_EYE_G': 255, 'L_EYE_B': 255}}
print(data)
client.write(json.dumps(data).encode('utf-8'))
client.close()

