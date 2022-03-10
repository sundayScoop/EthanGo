'''
EthanGo v1.0

Super simple socket program. No security. No privacy.
Do not run for prolonged periods of time.

Issues:
- Each sender must take turns sending messages
- Client will crash if server not up
- Simple terminal chat is not cool

Written by Julio Medeiros
10/03/2022
'''

import socket

version = 1.0

HOST = "127.0.0.1"   #input("Server's IP adress: ")  # The server's hostname or IP address
PORT = 14099  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
while True:
    msg = bytes(input("Me> "), "utf-8")  ## Get msg to send from user and convert into bytes
    s.sendall(msg)  ## Send message to server
    data = s.recv(1024) ## Receive any messages sent from server
    print("Them> ", data.decode("utf-8") ) ## Decode messages sent from server

print(f"Received {data!r}")