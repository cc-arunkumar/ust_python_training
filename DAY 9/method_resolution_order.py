class Employee:
    # Default method
    def perform_task(self):
        print("Employee is working in the Project")

# Class Manager Inherits from Employee
class Manager(Employee):
    def perform_task(self):
        print("Manager is Managing the team")

# Class Developer Inherits from Employee
class Developer(Employee):
    def perform_task(self):
        print("Developer is working on the project")

# Class tester Inherits from Employee
class Tester(Employee):
    def perform_task(self):
        print("Tester is looking for bugs in application")

#Creating object for those classes and storing
Employee=[Employee(),Manager(),Developer(),Tester()]


#iterating through the list and calling its methods
for i in Employee:
    i.perform_task()


