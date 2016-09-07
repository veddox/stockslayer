'''
StockSlayer is a multiplayer network game themed on the stock market.

This module houses the networking code, including the actual server.

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

import socket
import threading
import sys


#XXX Currently this is only an echo server

class Server:

    def __init__(self, port=29999):
        self.host = ""
        self.port = port
        self.server = None
        self.threads = []
        self.running = False

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error:
            if self.server: self.server.close()
            sys.exit("Failed to open socket.")

    def run(self):
        self.running = True
        self.open_socket()
        print("Server is running.")
        while self.running:
            client, address = self.server.accept()
            c = Client(client, address)
            c.daemon = True
            c.start()
            self.threads.append(c)
            for t in self.threads:
                if not t.is_alive():
                    self.threads.remove(t)
                    print("Removed an inactive server thread.")
        print("Closing server.")
        self.server.close()
        print("Joining remaining threads.")
        for thread in self.threads:
            thread.join()

class Client(threading.Thread):

    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.buffer_size = 4096 #arbitrary buffer limit

    def run(self):
        print("Connected to "+str(self.address))
        running = True
        while running:
            data = self.client.recv(self.buffer_size)
            if data:
                #Echo data back to the client
                data = bytes.decode(data)
                print("RECEIVED "+data)
                self.client.send(bytes("ECHO "+data, "utf-8"))
            else:
                print("Closing connection to "+str(self.address))
                self.client.close()
                running = 0
