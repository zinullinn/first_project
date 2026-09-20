"""Instance methods use self to work with object data."""


class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Not enough money"


# Here is an instance method changing an object's balance.
account = BankAccount("Arman", 5000)
print(account.deposit(1200))
print(account.withdraw(2000))
