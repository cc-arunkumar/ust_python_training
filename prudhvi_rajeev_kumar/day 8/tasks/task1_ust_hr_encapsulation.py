# #Question :
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

class Employee:
    def __init__(self, name, _department, __salary):
        self.name = name
        self._department = _department
        self.__salary = __salary
            
    def get_salary(self):
        print("Salary is : ", self.__salary)
        
    def show_info(self):
        print("Name is : ", self.name)
        print("Department is :", self._department)
    
    def update_salary(self, __amount):
        self.amount = __amount
        if self.amount > 0:
            self.__salary = self.amount
            
    def updated_salary(self):
        print("Updated Salary is : ",self.__salary)


e1 = Employee("Prudhvi", "HR", 50000)
e1.show_info()
e1.update_salary(75000)
e1.updated_salary()
try:
    print(e1.__salary)
except AttributeError:
    print("AttributeError: 'Employee' object has no attribute 'get_salary'")



#Console Output:
# Name is :  Prudhvi
# Department is : HR
# Updated Salary is :  75000
# AttributeError: 'Employee' object has no attribute 'get_salary'
    
