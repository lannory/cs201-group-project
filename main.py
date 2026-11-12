# Mykola Dietochka
from bikes import Bike, ElectroBike, Station
from client import Client
from take_return import Service
from finance import Finance


def main():
    station_a = Station("Station A")
    station_b = Station("Station B")
    stations = [station_a, station_b]

    station_a.return_bike(Bike(1))
    station_a.return_bike(ElectroBike(2))
    station_a.return_bike(Bike(3))

    station_b.return_bike(ElectroBike(4))
    station_b.return_bike(Bike(5))


    for station in stations:
        print("Station Name:", station.name, "Bikes available:", station.count_bikes())



    oleg = Client("Oleg")
    alex = Client("Alex")

    oleg.add_balance(200)
    alex.add_balance(300)

    clients = [oleg, alex]

    print("Curr balance:")
    for client in clients:
        print(f"{client.name}: {client.get_balance()}uah")
        