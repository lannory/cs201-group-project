
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
    def show_bikes(self):
        print(f"Станція: {self.name}")
        for bike in self.bikes:
            print(f"Номер: {bike.number}. Ціна за хвилину: {bike.price}")
    #показує станцію та номери байків в ній і ціну за хвилину
#це клас станції
