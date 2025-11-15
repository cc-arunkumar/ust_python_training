# Task: Method Resolution Order (MRO) demonstration

# Base class
class Employee:
    def perform_task(self):
        print("Generic employee task")

# Developer inherits from Employee but does not override perform_task
# So it will use the method from Employee
class Developer(Employee):
    pass

# Manager inherits from Employee and overrides perform_task
class Manager(Employee):
    def perform_task(self):
        print("Task is not done")

# Tester inherits from Employee and overrides perform_task
class Tester(Employee):
    def perform_task(self):
        print("Task is almost done")

# Create a list of different employee objects
employees = [Employee(), Manager(), Developer(), Tester()]

# Loop through each employee and call perform_task
# Python uses MRO to decide which method to call:
# - Manager → overridden method in Manager
# - Developer → inherits Employee’s method (since no override)
# - Tester → overridden method in Tester
for emp in employees:
    emp.perform_task()

    
#Sample Execution
# Generic employee task
# Task is not done
# Generic employee task
# Task is almost done
