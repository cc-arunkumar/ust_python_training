# Parent class
class Employee:
    def __init__(self):
        pass
    def perform_task(self):
        print("Task performed by Employee")
       
# Manager extends Employee class
class Manager(Employee):
    def perform_task(self):
        print("Task performed by Manager")
    
# Developer extends Employee class
class Developer(Employee):
    pass
        
# Tester extends Employee class
class Tester(Employee):
    pass
        
# Creating objects for all class and store it list
employee = [Employee(),Manager(),Developer(),Tester()]

# Looping through each objects
for i in employee:
    i.perform_task()
    
# output

# Task performed by Employee
# Task performed by Manager
# Task performed by Employee
# Task performed by Employee