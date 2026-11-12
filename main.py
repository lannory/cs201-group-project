import client from "client.py"
import bike from "bike.py"
import Service from "take_return.py"
import Station from "station.py"


def main():
    station_a = Station("Station A")
    station_b = Station("Station B")
    stations = [station_a, station_b]

    station_a.add(Bike(29))
    station_a.add(Bike(27))
    station_a.add(ElectricBike(29))

    station_b.add(Bike(26))
    station_b.add(ElectricBike(29))


    for station in stations:
        print("Station Name:", station.name, "Bikes available:", station.count())





    oleg = Client("Oleg")
    alex = Client("Alex")

    oleg.add_balance(200)
    alex.add_balance(300)

    clients = [oleg, alex]

    print("Curr balance:")
    for client in clients:
        print(f"{client.name}: {client.get_balance()}uah")



