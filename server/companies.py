'''
StockSlayer is a multiplayer network game themed on the stock market.

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

import xml.etree.ElementTree as xmlET

global companies
global events

companies, events = [], []

        
def new_company(name, industry, share_price):
    '''
    Create a new company and add it to the list.
    '''
    #XXX I think we should drop company ratings - they are probably unnecessary
    global companies
    company = dict(name=name, industry=industry, share=share_price, rating=0)
    companies.append(company)

def new_event(name, description, probability, impact,
              target_industry, whole_industry=False):
    '''
    Create a new event and add it to the list.
    '''
    global events
    event = dict(name=name, description=description, probability=probability,
                 impact=impact, target_industry=target_industry,
                 whole_industry=whole_industry)
    events.append(event)

def get_company(name):
    '''
    Return the desired company. Returns None if the company does not exist.
    '''
    global companies
    for c in companies:
        if c["name"] == name: return c
    return None

#XXX Do this with INI files? XML is too verbose...
def load_content(file_name):
    '''
    Load company and event definitions from an XML file.
    '''
    tree = xmlET.parse(file_name)
    # Load all companies
    for c in tree.findall("company"):
        cname = c.find("name").text
        cind = c.find("industry").text
        cprice = int(c.find("share").text)
        new_company(cname, cind, cprice)
    # Load all events
    for e in tree.findall("event"):
        ename = e.find("name").text
        edesc = e.find("description").text
        eprob = int(e.find("probability").text)
        eimp = int(e.find("impact").text)
        etarget = e.find("industry").text
        if e.find("industrywide"):
            ewhole = bool(e.find("industrywide").text)
        else: ewhole = False
        new_event(ename, edesc, eprob, eimp, etarget, ewhole)

load_content("content.xml") #DEBUG
    
# Create some companies
# DEPRECATED (as redundant and obsolete)
    
# new_company("Pear Computers", "Computer", 105)
# new_company("Nanosoft", "Computer", 60)
# new_company("Goggle", "Computer", 780)
# new_company("Dutsh Bank", "Finance", 15)
# new_company("JC Organ", "Finance", 30)
# new_company("X Combinator", "Finance", 10)
# new_company("Colditz Laboratories", "Pharmaceutics", 5)
# new_company("Baier", "Pharmaceutics", 95)
# new_company("Camgen", "Pharmaceutics", 155)
# new_company("Mapani Copper Mines", "Mining", 10)
# new_company("Australian Gold", "Mining", 5)
# new_company("Chemical & Mining Co.", "Mining", 25)

# new_company("Nile.com", "Logistics", 785)
# new_company("Bundespost", "Logistics", 30)
# new_company("Feedex", "Logistics", 165)
# new_company("AMW", "Automobile", 80)
# new_company("Rolls Ross", "Automobile", 135)
# new_company("Generic Motors", "Automobile", 30)

