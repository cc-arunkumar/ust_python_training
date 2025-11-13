# Encapsulation Task

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
# set_salary(amount)
# Allows updating salary only if amount is greater than zero
# show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)
# EXTRA CONDITION
# If someone tries:
# e.__salary
# It must FAIL (private attribute not accessible).




class Employee:
    def __init__(self):
        self.name = "Shakeel"
        self._department = "IT"
        self.__salary = 50000

    def get_salary(self):
        print(self.__salary) 

    def set_salary(self, amount):
        if amount > 0:
            self.__salary=amount
            print(amount)
        else:
            print("Invalid - salary is less than 0")

    def show_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Department: {self._department}")
    
emp1=Employee()
# emp1.set_salary(123)
print("Name :",emp1.name)
print("Department :",emp1._department)
print(emp1.__salary)

print("Trying to access private salary directly -> ERROR AttributeError: 'Employee' object has no attribute '__salary'.")

print("Salary :",emp1._Employee__salary)