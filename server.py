'''
EthanGo v1.1

Made for educational purposes only.

Written by Julio Medeiros
10/03/2022
'''

import os
import socket
import threading
import signal

### Creating a class for this isn't excatly necessary, but I prefer it. ###
class Server:
    version = 1.1

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 14099  # High port to evade scans

    s: socket.socket = None
    r_thread: threading.Thread = None
    s_thread: threading.Thread = None

    # Create a thread-safe event object to signal non-daeon threads to exit
    thread_end_event = threading.Event()

    def __init__(self):
        """Initalization"""

        # Register a signal handler to catch SIGINT (Ctrl+C)
        signal.signal(signal.SIGINT, self.exit_handler)

        print("Version: ", self.version, "\n")
        
        # Set the thread end event (on)
        self.thread_end_event.set()

        # Start the server
        self.start()

    def exit_handler(self, signum, frame):
        """ Handle SigInt (Ctrl+C) """
        print("\n\nHalting...")

        # Call shutdown
        self.shutdown()

    def receive(self, conn):
        # Loop until the thread end event is set
        while self.thread_end_event.is_set():
            data = conn.recv(1024) ## Receive messages from client
            if data:
                # Print their prompt, then their data, then our prompt.
                # Using end="" prevents a newline from being printed after the data
                # e.g. it overrides the "end" of the prompt which is usually a newline
                print("\nThem>%s\nMe> " % data.decode("utf-8"), end="" ) ## If data exists, decode and display
            else:
                print("\nConnection closed.")
                self.shutdown()
        

    def send(self, conn):
        while self.thread_end_event.is_set():
            # Print the prompt seperately from the input
            print("Me> ", end="")
            msg = bytes(input(""), "utf-8")  ## Collect msg to send from server in bytes
            conn.sendall(msg) ## Send msg to client

    def shutdown(self):
        # Clear the thread end event (off)
        self.thread_end_event.clear()

        print("Closing connection...")
        self.s.close()

        print("Exiting.")


        os._exit(os.EX_OK)

    def start(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()
        conn, addr = self.s.accept()

        self.threads = []
        # Daemon threads will exit when the main thread exits
        # This can be a problem if you have open resources, so
        # understanding how to properly open/close without daemon
        # is important.
        self.threads.append(threading.Thread(target=self.receive, args=(conn,)))
        self.threads.append(threading.Thread(target=self.send, args=(conn,)))

        # Start the threads
        for t in self.threads:
            t.start()
        
        # Wait for the threads to end
        for t in self.threads:
            t.join()

server = Server()
