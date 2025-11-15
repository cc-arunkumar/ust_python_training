# Python Polymorphism Task
# Task:
# Create a class Employee with a method perform_task().
# Then create three subclasses: Manager, Developer, and Tester.
# Requirements:
# - Override perform_task() in Manager and Tester to show role-specific behavior.
# - Do not override it in Developer (inherits base behavior).
# - Create a list of employee objects and loop through it to call perform_task() on each.
# Goal:
# Demonstrate polymorphism — same method name, different behavior based on object type.



class Employee:
    def __init__(self):
        pass
    def perform_task(self):
        print("Employee is Performing task")
        
# Manager is performing
        
class Manager(Employee):
    def perform_task(self):
        print("Task is being performed by manager")
        # print("manager is checking the task")
        
# Developer is performing   
class Developer(Employee):
    # def perform_task(self):
    #     # print("developer is writing the code")
      pass
        
# Tester is performing   
class Tester(Employee):
    def perform_task(self):
        print("Tester is checking the bug")
        
emp1 = [Employee(),Manager(),Developer(),Tester()]

for emp in emp1:
    emp.perform_task()
    
# Output
# Employee is Performing task
# Task is being performed by manager
# Employee is Performing task       
# Tester is checking the bug 
    