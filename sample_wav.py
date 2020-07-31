import client_io
import json
import os

ip = '192.168.11.x'
port = 22222
client = client_io.MyClient()
client.conect(ip, port)
with open('test.wav', 'rb') as f:
    data = f.read()
    client.write(data)
    recvmsg = client.read()
    print(len(recvmsg))
    client.close()
