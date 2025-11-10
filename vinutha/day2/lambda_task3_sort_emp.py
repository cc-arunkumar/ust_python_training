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

#code

employee=[("Rahul",3),("Priya",7),("karan",2),("Divya",5)]
employee.sort(key=lambda X:X[1])
print(employee)

#output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task3_dict.py
# [('karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
# PS C:\Users\303379\day2_training> 

