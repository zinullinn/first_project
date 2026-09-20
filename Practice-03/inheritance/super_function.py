"""super() calls a parent constructor."""


class Employee:
    """Store common employee data."""

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}."


class Developer(Employee):
    """Add a programming language to an employee."""

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


# Here is super() giving the child object its parent property.
developer = Developer("Nursultan", "Python")
print(f"{developer.name} codes in {developer.language}.")
print(developer.introduce())
