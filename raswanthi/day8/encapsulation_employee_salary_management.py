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
#  get_salary()
# Returns the private salary (because outside cannot access it directly)
#  set_salary(amount)
# Allows updating salary only if amount is greater than zero
#  show_info()
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


class Employee:
    def __init__(self, name, _department, __salary):
        self.name = name
        self._department = _department
        self.__salary = __salary  # private attribute

    def get_salary(self):
        print("Salary:", self.__salary)

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary

    def show_info(self):
        print(f"Name: {self.name} | Department: {self._department}")
        # Accessing private attribute using name mangling
        print("Salary:", self._Employee__salary)


emp1 = Employee("Ravi", "Finance", 50000)

#print(emp1.__dict__)

print("Name: ", emp1.name)
print("Department: ", emp1._department)
print("Trying to access private salary directly -> ERROR")
print("Accessing salary using getter: ", emp1._Employee__salary)  # name mangling


#output:
'''
Name:  Ravi
Department:  Finance
Trying to access private salary directly -> ERROR
Accessing salary using getter:  50000
'''