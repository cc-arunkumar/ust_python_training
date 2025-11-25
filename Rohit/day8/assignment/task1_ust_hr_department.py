# Scenario: UST HR Department – Employee Salary
# Management
# UST wants a very small internal Python module that handles employee salary
# safely.
# Why?
# Because salary is sensitive, and HR must protect it so:
# nobody can set salary to a negative number
# nobody can view salary without permission
# the internal raw salary value must not be exposed directly outside the class

# Define Employee class
class Employee:
    def __init__(self):
        # Public attribute (accessible anywhere)
        self.name = "Rohit"
        # Protected attribute (convention: should not be accessed outside class, but still possible)
        self._designation = "SDE-1"
        # Private attribute (name mangling makes it inaccessible directly outside the class)
        self.__salary = 50000
       
    # Getter method for private salary
    def get_salary(self):
        print(self.__salary)

    # Setter method for private salary with validation
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("salary is less than zero not acceptable")


# Create an Employee object
emp1 = Employee()

# Access public attribute directly
print("employee name ", emp1.name)

# Access protected attribute directly (possible but not recommended)
print("employee designation ", emp1._designation)

# Update salary using setter method
emp1.set_salary(75000)

# Access salary using getter method
emp1.get_salary()

# Try accessing private attribute directly (will raise AttributeError)
try:
    print(emp1.__salary)
except AttributeError:
    print("Trying to access private salary directly -> ERROR", AttributeError)

    
# ================sample output==============
# employee name  Rohit
# employee designation  SDE-1
# 75000
# Trying to access private salary directly -> ERROR <class 'AttributeError'>