class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Pas assez d'argent sur le compte.")
        self.balance -= amount

    def __str__(self):
        return f"Le compte a une balance de {self.balance} €."
