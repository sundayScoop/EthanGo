'''
EthanGo v1.1

Made for educational purposes only.

Written by Julio Medeiros
10/03/2022
'''

import socket
import threading

version = 1.1
print("Version: ", version, "\n")

HOST = "127.0.0.1"   #input("Server's IP adress: ")  # The server's hostname or IP address
PORT = 14099  # The port used by the server

def receive(conn):
    while True:
        data = conn.recv(1024) ## Receive messages from client
        if not data:  ## If data is null, connection broken > END
            break
        print("\nThem> ", data.decode("utf-8") ) ## If data exists, decode and display
    quit_flag = True

def send(conn):
    while True:
        msg = bytes(input("Me> "), "utf-8")  ## Collect msg to send from server in bytes
        conn.sendall(msg) ## Send msg to client

quit_flag = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))

r_thread = threading.Thread(target=receive, args=(s,), daemon=True)
r_thread.start()

s_thread = threading.Thread(target=send, args=(s,), daemon=True)
s_thread.start()

while not quit_flag:
    a=0
quit()