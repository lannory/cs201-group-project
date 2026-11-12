# Mykola Dietochka
from bikes_stations import Bike, ElectroBike, Station
from clients import Client
from cash import Finance
from take_return import Service


def admin_report(stations, finance):
    print("=== Report ===")
    for station in stations:
        print(f"  {station}")
    print(f"Total income {finance.get_income()} uah")


def main():
    print("=== Демо: прокат велосипедів ===\n")

    station_a = Station("A")
    station_b = Station("B")
    stations = [station_a, station_b]


    station_a.return_bike(Bike(1))
    station_a.return_bike(ElectroBike(2))
    station_a.return_bike(Bike(3))
    station_b.return_bike(ElectroBike(4, charge=80))
    station_b.return_bike(Bike(5))

    print("На старті:")
    for station in stations:
        print(f"{station}")
    print()

    oleg = Client("Олег", 200)
    alex = Client("Алекс", 300)
    clients = [oleg, alex]

    print("Баланс на старті:")
    for client in clients:
        print(f"{client.name}: {client.get_balance()} грн")
    print()

    finance = Finance()
    service = Service(finance)

    print("Поїздки:")

    bike = service.take_bike(oleg, station_a, 1)
    print(f"{oleg.name} взяв {bike} на станції {station_a.name}")
    bike = service.take_bike(alex, station_a, 2)
    print(f"{alex.name} взяв {bike} на станції {station_a.name}")

    cost = service.return_bike(oleg, station_b)
    print(f"{oleg.name} повернув велосипед на станцію {station_b.name}, списано {cost} грн")
    cost = service.return_bike(alex, station_b)
    print(f"{alex.name} повернув велосипед на станцію {station_b.name}, списано {cost} грн")

    bike = service.take_bike(oleg, station_a, 3)
    print(f"{oleg.name} взяв {bike} на станції {station_a.name}")
    cost = service.return_bike(oleg, station_b)
    print(f"{oleg.name} повернув велосипед на станцію {station_b.name}, списано {cost} грн")

    print("Спроба взяти велосипед на порожній станції:")
    bike = service.take_bike(alex, station_a, 1)
    if bike is None:
        print(f"{alex.name}: на станції {station_a.name} немає велосипедів "
              f"(залишилось: {station_a.count_bikes()}), спробуйте іншу станцію")
    else:
        print(f"{alex.name} взяв {bike}")


    print("Спроба взяти другий велосипед, не повернувши перший:")
    first = service.take_bike(oleg, station_b, 4)
    print(f"{oleg.name} взяв {first} на станції {station_b.name}")

    second = service.take_bike(oleg, station_b, 5)
    if second is False:
        print(f"{oleg.name}: вже має велосипед, другий взяти не можна")

    cost = service.return_bike(oleg, station_a)
    if cost is False:
        print(f"{oleg.name}: не вистачає грошей, велосипед ще у клієнта")
    else:
        print(f"{oleg.name} повернув велосипед №{first.number} на станцію "
              f"{station_a.name}, списано {cost} грн")

    print("Баланс після поїздок:")
    for client in clients:
        print(f"{client.name}: {client.get_balance()} грн")

    admin_report(stations, finance)

