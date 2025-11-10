#Task 3: Sort Employees by Experience
employees=[("Rahul",3),("Priya",7),("Karan",2),("Divya",5)]
sorted_employees=sorted(employees, key=lambda x:x[1])
print(sorted_employees)

#Sample output
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
