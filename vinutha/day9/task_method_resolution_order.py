# Method Resolution Order

# Base class Employee
class Employee:
    def perform_task(self):
        print("Employee: General work duties")  

# Child class Manager inherits from Employee
class Manager(Employee):
    def perform_task(self):
        print("Manager: Planning and supervising")  

# Example of overriding Developer class 
# class Developer(Employee):
#     def perform_task(self):
#         print("Developer: Writing and debugging code")

# Developer class without overriding perform_task
class Developer(Employee):
    pass   # Inherits perform_task from Employee (so it prints "Employee: General work duties")

# Child class Tester inherits from Employee
class Tester(Employee):
    def perform_task(self):
        print("Tester: Testing software and reporting bugs")  # Overrides perform_task with tester-specific duties

# Create a list of different employee objects
employees = [Employee(), Manager(), Developer(), Tester()]

# Loop through each employee and call perform_task
for emp in employees:
    emp.perform_task()  


# sample output:
# Employee: General work duties
# Manager: Planning and supervising
# Developer: Writing and debugging code
# Tester: Testing software and reporting bugs

# sample output: after using pass the child can inherits from the parents

# Employee: General work duties
# Manager: Planning and supervising
# Employee: General work duties
# Tester: Testing software and reporting bugs