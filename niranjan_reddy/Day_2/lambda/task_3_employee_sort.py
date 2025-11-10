# Task 3: Sort Employees by Experience

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


# Expected Output:
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]



employees = [
    ("Rahul", 3),
    ("Priya", 7),
    ("Karan", 2),
    ("Divya", 5)
]

employees.sort(key=lambda x:x[1])

print(employees)



# sample output

# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
