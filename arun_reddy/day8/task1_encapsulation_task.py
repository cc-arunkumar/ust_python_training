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

class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self._department=department
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
    def show_info(self):
        print(f"Name :{self.name}")
        print(f"Department:{self._department}")
        

e1=Employee("Arun","HR",90000)
e1.show_info()
e1.set_salary(89000)
#sample output or execution 
# Name :Arun
# Department:HR

# print("Salary:",e1.__salary)
print("Trying to access private salary directly -> ERROR")
#Traceback (most recent call last):
#   File "d:\ust_python_training\arun_reddy\day8\task1_encapsulation_task.py", line 56, in <module>
#     print("Salary:",e1.__salary)
#                     ^^^^^^^^^^^
# AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?
print("Accessing salary using getter:",e1.get_salary())
# Accessing salary using getter: 90000

e2=Employee("Felix","Finance",60000)
e2.show_info()
e2.set_salary(19000)
# print(e2.__salary)
print("Trying to access private salary directly -> ERROR")
print("Accessing salary using getter:",e2.get_salary())

# smaple ouput
# Name :Felix
# Department:Finance
# Trying to access private salary directly -> ERROR
# Accessing salary using getter: 19000