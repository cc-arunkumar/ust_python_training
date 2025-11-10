# Task 3: Sort Employees by Experience
# Requirement:
# You have a list of employees with their years of experience.
# Use a lambda function as the sorting key to sort them by experience in ascending order.

employees = [
    ("Rahul", 3),
    ("Priya", 7),
    ("Karan", 2),
    ("Divya", 5)
]

employees.sort(key=lambda x: x[1])
print(employees)

# Sample Output:
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
