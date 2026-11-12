#Yan Kalmus
from bikes_stations import Bike, Station
from cash import Finance
from clients import Client
import time

class Service():
    def __init__(self, finance: Finance, bike_minutes):
        self.finance = finance
        self.bike_minutes = {}

    def take_bike(self, station: Station, bike_number, bike_minutes):
        bike = station.take_bike(bike_number)
        bike_minutes[client.name] = time.time()
        return bike

    def return_bike(self, client: Client, station: Station):
        bike = client.bike_now
        if bike == None:
            return None
        minutes = bike_minutes[client.name] - time.time()
        cost = bike.calculate_cost(minutes)
        if not client.withdraw(cost):
            return False

        station.return_bike(bike)
        client.return_bike()
        self.finance.invoice(client, bike)
        return cost

