#MRO stands for Method Resolution Order in Python.

#class Employee
class Employee:
    def perform_task(self):
        print("Emploee : The manager, developer, and tester together complete the project")

#class Manger
class Manager(Employee):
    def perform_task(self):
        print(" Manger : The manager manages the team")

#child class of employee
class Developer(Employee):
    pass
    
#child class of employee    
class Tester(Employee):
    def perform_task(self):
        print( " Tester : The tester corrects the code")

# Create objects
emp = [Employee(), Manager(), Developer(), Tester()]

# Loop through each employee and call perform_task
for e in emp:
    e.perform_task()

# Emploee : The manager, developer, and tester together complete the project
#  Manger : The manager manages the team
# Emploee : The manager, developer, and tester together complete the project    

#  Tester : The tester corrects the code
