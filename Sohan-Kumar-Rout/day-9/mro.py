#Task Method Resolution Order

class Employee:
    def perform_task(self):
        print(" employee task")

class Developer(Employee):
    pass

class Manager(Employee):
    def perform_task(self):
        print("Attending meeting  done")

class Tester(Employee):
    def perform_task(self):
        print("Testing  done")

employees = [Employee(), Manager(), Developer(), Tester()]

for emp in employees:
    emp.perform_task()
    
#Sample Execution
# employee task
# Attending meeting  done
# employee task
# Testing  done