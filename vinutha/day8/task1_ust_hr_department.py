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
# Encapsulation Task 1
# __salary
# Salary MUST stay hidden from outside access.
# Should be accessible only using safe method.
# The Class MUST include 3 methods:
#  get_salary()
# Returns the private salary (because outside cannot access it directly)
# set_salary(amount)
# Allows updating salary only if amount is greater than zero
# show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)
# EXTRA CONDITION
# If someone tries:
# e.__salary
# It must FAIL (private attribute not accessible).


class Employeee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = None
        self.set_salary(salary)  # Use setter to validate

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount. Must be greater than zero.")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")



e = Employeee("Vinutha", "IT", 30000)

# Show public and protected info
e.show_info()

# Try accessing private attribute directly
try:
    print(e.__salary)  # This will raise an AttributeError
except AttributeError:
    print("Trying to access private salary directly error")

# Access salary using getter
print(f"Accessing salary using getter: {e.get_salary()}")


#output
# Name: Vinutha
# Department: IT
# Trying to access private salary directly error
# Accessing salary using getter: 30000
