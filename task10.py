class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}, hisobingizga {amount} so'm qo'shildi. Yangi balans: {self.balance} so'm.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}, hisobingizdan {amount} so'm yechildi. Yangi balans: {self.balance} so'm.")
        else:
            print(f"{self.owner}, hisobda yetarli mablag' mavjud emas! Balans: {self.balance} so'm.")

account1 = BankAccount("Ali", 500000)

account1.deposit(150000)     
account1.withdraw(200000)    
account1.withdraw(600000)    