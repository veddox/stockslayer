#!/usr/bin/python3
'''
StockSlayer is a multiplayer network game themed on the stock market.

This is the core logic module where the market simulation takes place.

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

import random

import companies

global actors
actors = []

# Randomly vary initial share prices using a Gauss distribution to
# prevent identical game starts.

for c in companies.companies:
    c["share"] = round(random.gauss(c["share"], c["share"]*0.05), 2)

    
def new_actor(name, money=1000, passwd=""):
    '''
    Create a new actor and add it to the list.
    '''
    global actors
    shares = {}
    #Each actor has a dict keeping track of the shares he owns in each company
    for c in companies.companies:
        shares[c["name"]] = 0
    actor = dict(name=name, money=money, password=passwd, shares=shares)
    actors.append(actor)

def get_actor(name, passwd=""):
    '''
    Find the actor of the given name. If no actor of that name is found or
    if the password doesn't match, return None.
    '''
    global actors
    for a in actors:
        if a["name"] == name:
            if a["password"] == passwd or a["password"] == "": return a
            else:
                print("Attempted access to actor "+str(name)+" - bad password.")
                return None
    return None
    
def buy(actor, company, amount):
    pass

def sell(actor, company, amount):
    pass

