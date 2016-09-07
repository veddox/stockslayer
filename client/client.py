#!/usr/bin/python3
'''
StockSlayer is a multiplayer network game themed on the stock market.

This is a simple commandline client for use during server development
(before we have a GUI client).

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

import socket

#XXX Currently this is only a very bare-bones echo client

host = 'localhost'
port = 29999
buffer_size = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    data = input("* ")
    if data == "quit" or data == "exit":
        s.send(bytes())
        break
    s.send(bytes(data, "utf-8"))
    rec = s.recv(buffer_size)
    print(bytes.decode(rec))

s.close()
