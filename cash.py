# Danylo Yusko

from datetime import time

from clients import Client
from bikes_stations import Bike

class Finance:
    def __init__(self):
        self.__total_income = 0 # For tracking total amount of income for admin
        
    def get_income(self):  # To get private total income
        return self.__total_income
    
    def invoice(self, user : Client, bike : Bike, time : time): # To invoice user after returning bike
        minutes = time.hour * 60 + time.minute + (1 if time.second else 0)
        price = bike.calculate_cost(minutes)
        user.withdraw(price)
        self.__total_income += price
        return