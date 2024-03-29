class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

class CheckingAccount(BankAccount):
    def __init__(self, balance, owner, overdraft_limit):
        super().__init__(balance, owner)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print("Withdrawal удачно")
        else:
            print("Withdrawal лимит превышен.")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit удачно.")

class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, interest_rate):
        super().__init__(balance, owner)
        self.interest_rate = interest_rate
    
    def accrue_interest(self):
        self.balance *= (1 + self.interest_rate)

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("Withdrawal удачно.")
        else:
            print("Нехватает для withdrawal.")