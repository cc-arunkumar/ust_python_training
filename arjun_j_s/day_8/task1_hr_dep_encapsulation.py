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
# Encapsulation Task 1
# __salary
# Salary MUST stay hidden from outside access.
# Should be accessible only using safe methods.
# The Class MUST include 3 methods:
# �� get_salary()
# Returns the private salary (because outside cannot access it directly)
# �� set_salary(amount)
# Allows updating salary only if amount is greater than zero
# �� show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)
# EXTRA CONDITION
# If someone tries:
# e.__salary
# It must FAIL (private attribute not accessible).
# DELIVERABLE
# Write code that:
# 1. Creates an employee,
# 2. Tries to access public, protected, and private attributes,
# Encapsulation Task 2
# 3. Uses safe methods to set and get salary,
# 4. Prints correct results,
# 5. Demonstrates encapsulation clearly.

#Define the parent class
class Employee:

    def __init__(self,name,dep,salary):
        self.name = name
        self._dep = dep #Set dep as protected
        self.__salary = salary #set salary as private

    def get_salary(self):
        print(f"Accessing salary using getter: {self.__salary}")
    
    def set_salary(self,amount):
        if amount>0:
            self.__salary = amount
            print("Salary Updated Successfully!!")
        else:
            print("Amount cannot be less than or equal to zero!!")
    
    def show_info(self):
        print(f"Name is : {self.name}")
        print(f"Department is : {self._dep}")
    
#Create an object    
emp = Employee("Arjun","IT",50000)
emp.show_info()
emp.get_salary()
emp.set_salary(0)
try:
    emp.__salary
except AttributeError:
    print("Trying to access private salary directly -> ERROR")
emp.set_salary(55000)
emp.get_salary()

#Output
# Name is : Arjun
# Department is : IT
# Accessing salary using getter: 50000
# Amount cannot be less than or equal to zero!!
# Trying to access private salary directly -> ERROR
# Salary Updated Successfully!!
# Accessing salary using getter: 55000