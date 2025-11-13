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
class Employee:
    def __init__(self):
        self.name="Nani"
        self._department="IT"
        self.__salary=70000
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid amount ")

    def show_info(self):
        print("Name:",self.name)
        print("Department:",self._department)
        print("salary:",self.__salary)
        
        

c1=Employee()
c1.set_salary(75000)
print("updated salary:",c1.get_salary())
c1.show_info()
# print(c1.__salary)

# print("Accessing salary using getter--",c1._Employee__salary)

# output
# Name: Nani
# Department: IT
# print("Trying to ccess private salary --- Error",AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?)
# Accessing salary using getter-- 75000

        