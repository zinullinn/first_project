"""Solutions for the Python classes tasks."""

from math import hypot


class StringHandler:
    """Read a string and print it in upper case."""

    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


class Shape:
    """A shape with area zero by default."""

    def area(self):
        return 0


class Square(Shape):
    """A square with equal side lengths."""

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    """A rectangle with length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Point:
    """Represent a point on a two-dimensional plane."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return hypot(self.x - other_point.x, self.y - other_point.y)


class Account:
    """A bank account that cannot have a negative balance."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True


if __name__ == "__main__":
    # Here is a short test of the class solutions.
    print(Shape().area())
    print(Square(4).area())
    print(Rectangle(4, 6).area())
    first_point = Point(1, 2)
    second_point = Point(4, 6)
    first_point.show()
    first_point.move(2, 3)
    print(first_point.dist(second_point))
    account = Account("Aruzhan", 1000)
    account.deposit(500)
    print(account.withdraw(300), account.balance)
    print(account.withdraw(2000), account.balance)
