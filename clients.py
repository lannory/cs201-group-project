# Yeva Menn
class Client:
# клас показує клієнта і його баланс
    def __init__(self, name: str, balance: float):
        #ініціалізація
        self.name = name
        self.balance = balance
        
    def deposit(self, amount: float):
        #поповнення балансу
        if amount <= 0:
            return False
        else:
            self.balance += amount
            return True
        
    def withdraw(self, amount: float):
        #списує кошти, якщо недостатньо виводить False
        if amount > self.balance or amount <= 0:
            return False
        else:
            self.balance -= amount
            return True
        
    def get_balance(self):
        #повертає поточний баланс
        return self.balance
