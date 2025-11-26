# Task 4_ Sort Employees by Experience
# You have a list of employees with their years of experience, and you need to sort them by experience in ascending order.

# Requirement:
# Use a lambda function as a sorting key.

# Example Input:

# employees = [
#     ("Rahul", 3),
#     ("Priya", 7),
#     ("Karan", 2),
#     ("Divya", 5)
# ]




employees = [
    ("Rahul",3),
    ("Priya",7),
    ("Karan",2),
    ("Divya",5),
]

employees.sort(key=lambda exp: exp[1])
print(employees)

# Sort Employees by Experience.py"
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]