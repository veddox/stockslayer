'''
StockSlayer is a multiplayer network game themed on the stock market.

Copyright (c) 2016 by Daniel Vedder and Niklas Götz.
Licensed under the terms of the MIT license.
'''

global companies
global industries
global events

companies, events = [], []

#XXX Do we really need this list?
industries = ["Computer", "Mining", "Finance", "Pharmaceutics",
              "Automobile", "Logistics"]


# Class definitions

class Company:
    '''
    This class represents a company trading on the stock market.
    '''

    def __init__(self, name, industry, share_price):
        global industries
        self.name = name
        if industry in industries:
            self.industry = industry
        else:
            sys.exit("Industry not recognized: "+str(industry))
        self.share = share_price
        self.rating = 0

    def change_rating(self, amount):
        self.rating = self.rating + amount

    def change_share_price(self, amount):
        #XXX Shouldn't this be calculated based on the rating?
        self.share = self.share + amount


class Event:
    '''
    An event is a random happening that influences the rating 
    of one or more companies.
    '''

    def __init__(self, name, description, probability, impact,
                 target_industry, whole_industry=False):
        self.name = name
        # $COMPANY in the description will be replaced with the
        # company name
        self.description = description
        self.probability = probability
        self.target_industry = target_industry
        self.whole_industry = whole_industry


#TODO Read in companies and events from a seperate file
        
def new_company(name, industry, share_price):
    '''
    Create a new company and add it to the list.
    '''
    global companies
    companies.append(Company(name, industry, share_price))

def new_event(name, description, probability, impact,
              target_industry, whole_industry=False):
    '''
    Create a new event and add it to the list.
    '''
    global events
    events.append(Event(name, description, probability, impact,
                        target_industry, whole_industry))

    
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

