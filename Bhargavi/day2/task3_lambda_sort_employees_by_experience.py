#Sort Employees by Experience
employees = [("Meena", 3),("Vani", 7),("Sri", 2),("bhanu", 5)]
sorted_employees = sorted(employees, key=lambda x: x[1])
print(sorted_employees)

# [('Sri', 2), ('Meena', 3), ('bhanu', 5), ('Vani', 7)]