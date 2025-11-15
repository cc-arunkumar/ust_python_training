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
# Your Output Should Look Something Like:
# Name: Arun
# Department: IT
# Trying to access private salary directly -> ERROR
# Accessing salary using getter: 75000
# Encapsulation Task 3


class Employee:
    def __init__(self, name, _department, __salary):
        # Public attribute
        self.name = name
        # Protected attribute (by convention)
        self._department = _department
        # Private attribute (name mangled)
        self.__salary = __salary

    # Getter method for private salary
    def getsalary(self):
        return self.__salary  # Return the value instead of printing

    # Setter method for salary with validation
    def setsalary(self, amount):
        if amount > 0:
            self.__salary = amount  # Corrected to update the private attribute
            print(f"Updated salary is {amount}")
        else:
            print("Invalid amount! Salary should be greater than 0")

    # Method to display employee info
    def show_info(self):
        print(f"Name: {self.name}, Department: {self._department}")
        print(f"Salary: {self.__salary}")  # Accessing private variable within class
# Create an employee object
emp1 = Employee("Taniya", "IT", 50000)

# Show basic info
emp1.show_info()

# Attempt to access private attribute directly (will raise error)
try:
    print(emp1.__salary)
except AttributeError:
    print("Trying to access private salary directly = ERROR")

# Update salary using setter
emp1.setsalary(60000)

# Access salary using getter
print(f"Accessing salary using getter: {emp1.getsalary()}")

# Output    
# Name: Taniya, Department: IT
# Salary: 50000
# Trying to access private salary directly = ERROR
# Updated salary is 60000
# Accessing salary using getter: 60000    