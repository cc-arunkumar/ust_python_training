# Method Overriding

class Employee:
    def work(self):
        print("Employee is doing generic day to day work")

class Developer(Employee):
    def work(self):
        print("Developer is completing the code for project")

class Manager(Employee):
    def work(self):
        print("Manager manages the project requirements")

emp1 = Employee()
emp2 = Developer()
emp3 = Manager()

emp1.work()
emp2.work()
emp3.work()      

# ---------------------------------------------------------------------------------

# Sample Output

# Employee is doing generic day to day work
# Developer is completing the code for project
# Manager manages the project requirements