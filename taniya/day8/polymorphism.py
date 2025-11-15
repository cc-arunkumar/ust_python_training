# 🧩 Question:
# Create a base class Employee with a method work().
# Create two subclasses: Developer and Manager, both overriding the work() method.
# Create objects of each class and call the work() method to demonstrate polymorphism.

# Base class definition
class Employee:
    # Method to show generic employee work behavior
    def work(self):
        print("Employee is working")

# Subclass Developer inherits from Employee
class Developer(Employee):
    # Overriding work() method to show developer-specific behavior
    def work(self):
        print("Developer is working")

# Subclass Manager inherits from Employee
class Manager(Employee):
    # Overriding work() method to show manager-specific behavior
    def work(self):
        print("Manager is working")

# Creating an object of Employee
e1 = Employee()

# Creating an object of Developer
d1 = Developer()

# Creating an object of Manager
m1 = Manager()

# Calling work() method on Employee object
e1.work()  # Output: Employee is working

# Calling work() method on Developer object
d1.work()  # Output: Developer is working

# Calling work() method on Manager object
m1.work()  # Output: Manager is working

# Output
# Employee is working
# Developer is working
# Manager is working 