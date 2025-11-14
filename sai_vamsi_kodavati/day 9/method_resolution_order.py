# MRO --> Method Resolution Order

# Creating a class called Employee
class Employee:
    def perform_tasks(self):
        print("Employee is working on generic day to day tasks")

# Creating a class Manager which inherits from Employee
class Manager(Employee):
    def perform_tasks(self):
        print("Manager managing the tasks")
        print("Managing the projects")
        print("Managing the client calls")

class Developer(Employee):
    pass
        # def perform_tasks(self):
        #      print("Developer writing the code")
        #      print(" Ensuring to write a optimized code")
             
    
class Tester(Employee):
    def perform_tasks(self):
        print("Testing the code")
        print("Finding out the bugs in the code")


e1 = Employee()
e2 = Manager()
e3 = Developer()
e4 = Tester()

emp = [e1,e2,e3,e4]

for i in emp:
    i.perform_tasks()
    print("-" * 50)

# Sample Output

# Employee is working on generic day to day tasks
# --------------------------------------------------
# Manager managing the tasks
# Managing the projects
# Managing the client calls
# --------------------------------------------------
# Developer writing the code
# Ensuring to write a optimized code
# --------------------------------------------------
# Testing the code
# Finding out the bugs in the code
# --------------------------------------------------