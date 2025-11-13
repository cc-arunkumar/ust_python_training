#  UST HR Department – Employee Salary Management
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
# get_salary()
# Returns the private salary (because outside cannot access it directly)
# set_salary(amount)
# Allows updating salary only if amount is greater than zero
# show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)

# EXTRA CONDITION
# If someone tries:
# e.__salary
# It must FAIL (private attribute not accessible)

class Employee:
    def __init__(self,name,designation,salary):
        self.name = name
        self._designation = designation
        self.__salary = salary
        
    def get_salary(self):
        print("Accessing salary using getter: ",self.__salary)
    
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary = new_salary
            print("Salary Updated Succesfully!")

        else:
            print("Salary wont be less than Zero")
            
    def show_info(self):
        print("Name:",self.name)
        print("Designation:",self._designation)

a1 = Employee('Anjan','SDE-1',60000)
a1.set_salary(90000)
a1.show_info()
a1.get_salary()
# print(a1.__salary) AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?
print("Trying to access private salary directly -> AttributeError: Employee object has no attribute __salary")

#Sample Output
# Salary Updated Succesfully!
# Name: Anjan
# Designation: SDE-1
# Accessing salary using getter:  90000
# Trying to access private salary directly -> AttributeError: Employee object has no attribute __salary

