# Encapsulation Task
# Scenario: UST HR Department – Employee Salary
# Management
# UST wants a very small internal Python module that handles employee salary
# safely.
# Why?
# Because salary is sensitive, and HR must protect it so:
# nobody can set salary to a negative number
# nobody can view salary without permission
# the internal raw salary value must not be exposed directly outside the class
# TASK REQUIREMENT
# You must create a class Employee with THREE attributes:
# 1. Public attribute
# name
# Anyone in the company can see the employee's name.
# 2. Protected attribute
# _department
# Other teams should not directly change the employee’s department,
# but HR tools inside the system can access it.
# 3. Private attribute
# __salary
# Salary MUST stay hidden from outside access.
# Should be accessible only using safe methods.

# EXTRA CONDITION
# If someone tries:
# e.__salary
# It must FAIL (private attribute not accessible).
# DELIVERABLE
# Write code that:
# 1. Creates an employee,
# 2. Tries to access public, protected, and private attributes,
# 3. Uses safe methods to set and get salary,
# 4. Prints correct results,
# 5. Demonstrates encapsulation clearly.
# Your Output Should Look Something Like:
# Name: Arun
# Department: IT
# Trying to access private salary directly -> ERROR
# Accessing salary using getter: 75000

class Employee:
    def __init__(self):
        self.name="Shanker"
        self._department="SAS"
        self.__salary=200000


# The Class MUST include 3 methods:
    def get_salary(self):
        return self.__salary

    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
            print(f"Salary updated to:{self.__salary}")
        else:
            print("Invalid salary")
        
    def show_info(self):
        print(f"Employee name:{self.name}")
        print(f"Employee department:{self._department}")

emp1=Employee()
print(f"Employee salary:{emp1.get_salary()}")
emp1.set_salary(300000)
emp1.show_info()



# Sample output:
# emp1.__salary
# AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?

# Employee salary:200000
# Salary updated to:300000
# Employee name:Shanker
# Employee department:SAS

