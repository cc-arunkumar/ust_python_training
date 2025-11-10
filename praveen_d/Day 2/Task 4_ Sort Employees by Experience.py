# Task 4_ Sort Employees by Experience



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