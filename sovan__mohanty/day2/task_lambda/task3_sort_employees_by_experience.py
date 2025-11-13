#Sort Employees by Experience
employees=eval(input("Enter the employees with experience"))
employees.sort(key=lambda x:x[1])
print(employees)

#Sample Executions
# Enter the employees with experience[('Karan',2),('Rahul',3),('Divya',5),('Priya',7)]
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
