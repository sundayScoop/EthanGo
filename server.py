'''
EthanGo v1.2

Made for educational purposes only.

Written by Julio Medeiros
18/03/2022
'''

import socket
import threading

version = 1.1
print("Version: ", version, "\n")
print("Enter 'end' to exit program\n")

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 14099  # High port to evade scans

quit_flag = False

def receive(conn):
    while True:
        try: data = conn.recv(1024) ## Receive messages from client
        except:
            break
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
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

r_thread = threading.Thread(target=receive, args=(conn,), daemon=True)
r_thread.start()

s_thread = threading.Thread(target=send, args=(conn,), daemon=True)
s_thread.start()
   

while not quit_flag:
    a=0
print("\nExiting...")
quit()
