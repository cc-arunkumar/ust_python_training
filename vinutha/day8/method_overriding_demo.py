# method overriding
# Base class Employee
class Employee:
    def work(self):
        # Generic work method for any employee
        print("Employee is working on generic day to day task")


# Derived class Developer inherits from Employee
class Developer(Employee):
    def work(self):
        # Overriding the work() method for Developer
        print("Developer is coding the requirement")


# Derived class Manager inherits from Employee
class Manager(Employee):
    def work(self):
        # Overriding the work() method for Manager
        print("Managing project Modules")


# Create objects of each class
e1 = Employee()   # Object of base class
d1 = Developer()  # Object of Developer class
m1 = Manager()    # Object of Manager class

# Call work() method on each object
e1.work()   # Calls Employee's work()
d1.work()   # Calls Developer's overridden work()
m1.work()   # Calls Manager's overridden work()


# sample output

# Employee is working on generic day to day task
# Developer is coding the requirement
# Managing project Modules

