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

class Employee:
    
    def __init__(self,name,department,salary):
        #public 
        self.name=name
        #protected
        self._department=department
        #private
        self.__salary=salary
    #The Class MUST include 3 methods:
    # �� get_salary()
    # Returns the private salary (because outside cannot access it directly)
    def get_salary(self):
        return self.__salary
    
    # �� set_salary(amount)
    # Allows updating salary only if amount is greater than zero
    
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
    # �� show_info()
    # Prints name + department
    # But MUST NOT print salary directly (salary is private
    
    def show_info(self):
        print("Name: ",self.name)
        print("Demaprtment: ",self._department)

emp1=Employee("shyam","IT",90000)
emp1.show_info()
# emp1.__salary       AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?

emp1.set_salary(425000)
print("Accessing salary using getter:",emp1.get_salary())

#Sample output
# Name:  shyam
# Demaprtment:  IT
# Accessing salary using getter: 425000