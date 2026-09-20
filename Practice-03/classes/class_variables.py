"""Class variables are shared; instance variables belong to one object."""


class Course:
    """Store a course with a shared school name."""

    school_name = "Steppe University"

    def __init__(self, title):
        self.title = title


# Here is the difference between shared and instance data.
python_course = Course("Python")
math_course = Course("Math")
python_course.school_name = "Online Academy"
print(python_course.school_name, python_course.title)
print(math_course.school_name, math_course.title)
