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

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 14099  # High port to evade scans

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024) ## Receive messages from client
        if not data:  ## If data is null, connection broken > END
            break
        print("Them> ", data.decode("utf-8") ) ## If data exists, decode and display
        msg = bytes(input("Me> "), "utf-8")  ## Collect msg to send from server in bytes
        conn.sendall(msg) ## Send msg to client
