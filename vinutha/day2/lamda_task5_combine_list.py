# Task 5: Combine Two Lists (Employee and Department)
# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.

#code

names=['Arun','Neha','Vikram']
depts=['HR','IT','Finance']
result=list(map(lambda X,Y:f"{X} works in {Y}",names,depts))
print(result)
# Create a list of employee names
names = ['Arun', 'Neha', 'Vikram']

# Create a list of departments corresponding to each employee
depts = ['HR', 'IT', 'Finance']

# Use the map() function with a lambda to combine names and departments
# lambda X, Y: f"{X} works in {Y}" → takes a name (X) and a department (Y),
# and returns a formatted string like "Arun works in HR"
# map() pairs elements from 'names' and 'depts' one by one
# list() converts the map object into a list of strings
result = list(map(lambda X, Y: f"{X} works in {Y}", names, depts))

# Print the final list of strings
print(result)

# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task5_combineList.py
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']
# PS C:\Users\303379\day2_training> 

