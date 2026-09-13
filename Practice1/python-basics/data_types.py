course = "Programming Principles"
semester = 3
grade = 95.5
completed = True
subjects = ["Python", "Git"]

for value in (course, semester, grade, completed, subjects):
    print(value, "->", type(value).__name__)
