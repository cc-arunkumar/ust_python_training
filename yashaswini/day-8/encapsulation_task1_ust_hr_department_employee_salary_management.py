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
    def __init__(self, name, department, salary):
        self.name=name
        self._department=department
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount>0:
            self._salary=amount
        else:
            print("salary must be greater than zero")
            
    def show_info(self,):
        print("Name: ",self.name)
        print("Department: ",self._department)
        
e = Employee("Yashaswini", "IT", 55000)

# Show public + protected info
e.show_info()

# Instead of crashing, we simulate the failed access
print("Trying to access private salary directly -> ERROR")

# Update salary safely
e.set_salary(75000)

# Access salary using getter
print("Accessing salary using getter:", e.get_salary())


#o/p:
# Name:  Yashaswini
# Department:  IT
# Trying to access private salary directly -> ERROR
# Accessing salary using getter: 55000