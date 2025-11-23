# Task 2:Mathod resolution order

class Employee():
    def perform_task(self):
        print("Task has been started to perform...........")

class Manager(Employee):
     def perform_task(self):
        print("Manager insist to perform the task")

class Developer(Employee):
    pass
    #  def perform_task(self):
    #     print("Developer started the task")

class Tester(Employee):
     def perform_task(self):
        print("Tester started to work on the task")
print("--------------------------------------")
print("After we take the process form Developer")
employee=[Employee(),Manager(),Developer(),Tester()]

for emp in employee:
    emp.perform_task()

# Sample output:
# Before we take the process form Developer
# Task has been started to perform...........
# Manager insist to perform the task
# Developer started the task
# Tester started to work on the task

# --------------------------------------
# After we take the process form Developer
# Task has been started to perform...........
# Manager insist to perform the task
# Task has been started to perform...........
# Tester started to work on the task