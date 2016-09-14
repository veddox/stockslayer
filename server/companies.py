'''
StockSlayer is a multiplayer network game themed on the stock market.

This module creates all game companies and events.

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

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

def new_event(name, impact, target_industry, probability=0.01,
              whole_industry=False):
    '''
    Create a new event and add it to the list.
    '''
    global events
    event = dict(name=name, probability=probability, impact=impact,
                 target_industry=target_industry,
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


#
# CONTENT
#

# Create some companies
    
new_company("Pear Computers", "Computer", 105)
new_company("Nanosoft", "Computer", 60)
new_company("Goggle", "Computer", 780)
new_company("Dutsh Bank", "Finance", 15)
new_company("JC Organ", "Finance", 30)
new_company("X Combinator", "Finance", 10)
new_company("Colditz Laboratories", "Pharmaceutics", 5)
new_company("Baier", "Pharmaceutics", 95)
new_company("Camgen", "Pharmaceutics", 155)
new_company("Mapani Copper Mines", "Mining", 10)
new_company("Australian Gold", "Mining", 5)
new_company("Chemical & Mining Co.", "Mining", 25)
new_company("Nile.com", "Logistics", 785)
new_company("Bundespost", "Logistics", 30)
new_company("Feedex", "Logistics", 165)
new_company("AMW", "Automobile", 80)
new_company("Rolls Ross", "Automobile", 135)
new_company("Generic Motors", "Automobile", 30)


# Create some events

new_event("%NAME% buys a hot new startup.", 5, "Computer")
new_event("%NAME% networks were breached in a hacker attack.", -5, "Computer")
new_event("%NAME% is accused of trying to manipulate the stock market.",
          -5, "Finance")
new_event("%NAME% has just received a triple-A rating.", 5, "Finance")
new_event("%NAME%'s researchers have discovered a new cancer treatment.",
          5, "Pharmaceutics")
new_event("One of %NAME%'s drugs has undisclosed side effects.",
          -5, "Pharmaceutics")
new_event("%NAME%'s engineers have discovered a rich mineral deposit.",
          5, "Mining")
new_event("Miners trapped underground in a %NAME% accident.", -5, "Mining")
new_event("A new procedure enables %NAME% to deliver goods even faster.",
          5, "Logistics")
new_event("A strike cripples %NAME%'s transport network.", -5, "Logistics")
new_event("%NAME% introduces a new series of electric sports cars.",
          5, "Automobile")
new_event("%NAME% has to lay off workers from one of their factories.",
          -5, "Automobile")
