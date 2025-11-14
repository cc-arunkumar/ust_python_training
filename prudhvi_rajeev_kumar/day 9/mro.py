class Employee:
    def __init__(self):
        pass        
    def perform_task(self):
        print("Employee is Performing its task")

class Developer(Employee):
    pass
    
class Manager(Employee):        
    def perform_task(self):
        print("Manager Completed the task")
    
class Tester(Employee):        
    def perform_task(self):
        print("Tester Completed the Task")


employees = [Employee(), Developer(), Manager(), Tester()]
for emp in employees:
    emp.perform_task()

#Console Output:
# Employee is Performing its task
# Employee is Performing its task
# Manager Completed the task
# Tester Completed the Task