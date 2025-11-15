# Method Resolution Order

class Employee:
    def perform_task(self):
        print("Employee: General work duties")
# child classes of employee
class Manager(Employee):
    def perform_task(self):
        print("Manager: Planning and supervising")

# class Developer(Employee):
#     def perform_task(self):
#         print("Developer: Writing and debugging code")
        
class Developer(Employee):
    pass

class Tester(Employee):
    def perform_task(self):
        print("Tester: Testing software and reporting bugs")

employees=[Employee(),Manager(),Developer(),Tester()]
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