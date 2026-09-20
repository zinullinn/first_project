"""The __init__ constructor creates instance data."""


class Student:
    """Store a student's name and score."""

    def __init__(self, name, score):
        self.name = name
        self.score = score


# Here is a constructor call that sets object properties.
student = Student("Mira", 92)
print(f"{student.name}: {student.score}")

# Here is modifying and deleting an object property.
student.score = 95
del student.name
print(student.score)
