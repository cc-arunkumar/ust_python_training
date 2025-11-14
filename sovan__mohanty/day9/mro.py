#Task Method Resolution Order

class Employee:
    def perform_task(self):
        print("Generic employee task")

class Developer(Employee):
    pass

class Manager(Employee):
    def perform_task(self):
        print("Task is not done")

class Tester(Employee):
    def perform_task(self):
        print("Task is almost done")

employees = [Employee(), Manager(), Developer(), Tester()]

for emp in employees:
    emp.perform_task()
    
#Sample Execution
# Generic employee task
# Task is not done
# Generic employee task
# Task is almost done
