#parent class
class Employee:
    def work(self):
        print("Employee is working")

#child class - 1
class Manager(Employee):
    def work(self):
        print("Manager is managing projects")

#child class - 2       
class Developer(Employee):
    def work(self):
        print("Developer is writing code")

#child class - 3     
class Tester(Employee):
    def work(self):
        print("Tester is finding bugs")

#creating list for all class
employees = [Employee(), Developer(), Tester(), Manager()]

#printing through loop
for emp in employees:
    emp.work()

#sample output

# Employee is working
# Developer is writing code
# Tester is finding bugs
# Manager is managing projects
