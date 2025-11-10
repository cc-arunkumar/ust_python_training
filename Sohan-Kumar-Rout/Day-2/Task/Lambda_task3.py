#Task3: Sorting based upon the Experience of the employee 

#Code
employees=[("Rahul",3), ("Priya",7), ("Karan",2),("Divya",5)]
employees.sort(key = lambda x : x[1])
print(employees)

#Output
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]

