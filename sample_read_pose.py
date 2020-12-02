import client_io
import json
import os
import time

ip = '192.168.0.60'
port = 22225
client = client_io.MyClient()
client.connect(ip, port)
data = client.read()
print(data.decode('utf-8'))
client.close()
