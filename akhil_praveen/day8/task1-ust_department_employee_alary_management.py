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
# Should be accessible only using safe methods
# The Class MUST include 3 methods:
# �� get_salary()
# Returns the private salary (because outside cannot access it directly)
# �� set_salary(amount)
# Allows updating salary only if amount is greater than zero
# �� show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)

class Employee:
    def __init__(self,name,dept,salary):
        self.name = name
        self._department = dept
        self.__salary = salary
    
    def get_salary(self):
        return  f"Salary accessed using getter:{self.__salary}"
    
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("Salary cannot be zero")
        
    def show_info(self):
        print("Name: ",self.name)
        print("Designation: ",self._department)

emp1 = Employee("Akhil","IT",50000)


emp1.show_info()
print(emp1.get_salary())
emp1.set_salary(0)
emp1.set_salary(100000)
emp1.get_salary()
try:
    print(emp1.__salary)
except AttributeError:
    print("Trying to access private salary directly -> ERROR")

# output
# Name:  Akhil
# Designation:  IT
# Salary accessed using getter:50000
# Salary cannot be zero
# Trying to access private salary directly -> ERROR