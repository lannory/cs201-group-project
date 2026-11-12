
# Bohdan Kalinichenko
class Station:
    def __init__(self, name):
        self.name = name
        self.bikes = []
    #атрибути
    def return_bike(self, bike):
        self.bikes.append(bike)
    #повернути велік
    def take_bike(self, number):
        for bike in self.bikes:
            if bike.number == number:
                self.bikes.remove(bike)
                return bike
        return None
    #взяти велік
    def count_bikes(self):
        return len(self.bikes)
    #функція рахує загальну кількість веліків
    def __str__(self):
        return f"Станція {self.name}, велосипедів: {len(self.bikes)}"
    #показує станцію та кількість веліків в ній
#це клас станції
class Bike:
    def __init__(self, number):
        self.number = number
        self.price = 2
    def calculate_cost(self, minutes):
        return minutes * self.price
    def __str__(self):
        return f"Номер: {self.number}, тип: звичайний"
    #рахуєм ціну оренди веліка
#клас веліка
class ElectroBike(Bike):
    def __init__(self, number, charge=100):
        super().__init__(number)
        self.price = 5
        self.charge = charge
    def __str__(self):
        return f"Номер: {self.number}, тип: електричний, заряд: {self.charge}"
#клас електровеліка