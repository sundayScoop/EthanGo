'''
EthanGo v1.2

Made for educational purposes only.

Written by Julio Medeiros
18/03/2022
'''

import socket
import threading

version = 1.2
print("Version: ", version, "\n")
print("Enter 'end' to exit program\n")

HOST = "127.0.0.1"   #input("Server's IP adress: ")  # The server's hostname or IP address
PORT = 14099  # The port used by the server

quit_flag = False

def receive(conn):
    while True:
        try: data = conn.recv(1024) ## Receive messages from client
        except:
            break ## If error is thrown due to other client disconnecting
        print("\nThem> ", data.decode("utf-8") ) ## If data exists, decode and display
    global quit_flag
    quit_flag = True

def send(conn):
    while True:
        msg = bytes(input("Me> "), "utf-8")  ## Collect msg to send from server in bytes
        if msg == b'end':
            conn.close()
            break
        conn.sendall(msg) ## Send msg to client


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))


r_thread = threading.Thread(target=receive, args=(s,), daemon=True)
r_thread.start()

s_thread = threading.Thread(target=send, args=(s,), daemon=True)
s_thread.start()

while not quit_flag:
    a=0
print("\nExiting...")
quit()