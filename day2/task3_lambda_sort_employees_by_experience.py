#Sort Employees by Experience
employees = [
    ("varsha", 3),
    ("yashu", 7),
    ("harthi", 2),
    ("bhargavi", 5)
]
sorted_employees = sorted(employees, key=lambda x: x[1])
print(sorted_employees)

#sample execution
#[('harthi', 2), ('varsha', 3), ('bhargavi', 5), ('yashu', 7)]
