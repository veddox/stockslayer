#!/usr/bin/python3
'''
StockSlayer is a multiplayer network game themed on the stock market.

This is the main server module.

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

import sys
from threading import Thread
from server import *

def init():
    s = Server()
    server_thread = Thread(target=s.run)
    server_thread.daemon = True
    server_thread.start()
    print("Waiting for input.")
    while True:
        cancel = input()
        if cancel:
            s.running = False
            break
    print("Goodbye!")
    sys.exit()

if __name__ == '__main__':
    init()
