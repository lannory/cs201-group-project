# Danylo Yusko

from datetime import datetime, time

from clients import Client
from bikes_stations import Bike

class Finance:
    def __init__(self):
        self.__total_income = 0 # For tracking total amount of income for admin
        
    def get_income(self):  # To get private total income
        return self.__total_income
    
    def invoice(self, user : Client, bike : Bike): # To invoice user after returning bike
        pass
        
            
