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
# The Class MUST include 3 methods:
# �� get_salary()
# Returns the private salary (because outside cannot access it directly)
# �� set_salary(amount)
# Allows updating salary only if amount is greater than zero
# �� show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)


class Employee:
    def __init__(self):
        # public --> No restriction 
        self.name = "Felix"
        
        # protected --> Convension : Should not be accessed outside the class or subclass
        self._depatment = "IT"
        
        # private --> Nmae mangaling :cannot be accessed directly outside the class
        self.__salary = 50000
        
    def get_salary(self):
        print("Salary : ",self.__salary)
        
    def set_salary(self,new_salary):
        self.__salary = new_salary
        print("Salary Updated: ",self.__salary)
        
    def show_info(self):
        print("Name: ",self.name)
        print("Department: ",self._depatment)
        print("Salary: ",self.__salary)
        
emp1 = Employee()
emp1.get_salary()
print("----------------------")
emp1.show_info()
emp1.set_salary(60000)
print("----------------------")
print("Name: ",emp1.name)
print("Designation: ",emp1._depatment) # Should't be accessed

try:
    print("Salary: ",emp1.__salary)  # Not accessible with same name, accessible using mangled name(_ClassName__varname)
except :
    print("Trying to access private salary directly -> ERROR")


print("Salary: ",emp1._Employee__salary)

# output

# Salary :  50000
# ----------------------
# Name:  Felix
# Department:  IT
# Salary:  50000
# Salary Updated:  60000
# ----------------------
# Name:  Felix
# Designation:  IT
# Trying to access private salary directly -> ERROR
# Salary:  60000