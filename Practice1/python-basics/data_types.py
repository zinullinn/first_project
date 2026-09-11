# W3Schools: Python Data Types
course = "Programming Principles"  # str
semester = 3  # int
grade = 95.5  # float
completed = True  # bool
subjects = ["Python", "Git"]  # list

for value in (course, semester, grade, completed, subjects):
    print(value, "->", type(value).__name__)
