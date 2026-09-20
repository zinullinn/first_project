"""A child class inherits from a parent class."""


class Animal:
    """Represent a general animal."""

    def eat(self):
        return "The animal is eating."


class Cat(Animal):
    """Represent a cat that inherits from Animal."""

    def meow(self):
        return "The cat says meow."


# Here is a child object using its own and inherited methods.
pet_cat = Cat()
print(pet_cat.eat())
print(pet_cat.meow())
