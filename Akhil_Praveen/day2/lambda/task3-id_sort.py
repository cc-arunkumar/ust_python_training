# id_sort
employees = [
    ("Rahul", 3),
    ("Priya", 7),
    ("Karan", 2),
    ("Divya", 5)
]
employees.sort(key=lambda emp:emp[1])
print(employees)

# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]