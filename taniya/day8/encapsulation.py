# 🧩 Question:
# Create a class `Employee` with public, protected, and private attributes.
# Implement a method `show()` to display all attributes.
# Demonstrate encapsulation by using name mangling for the private attribute.

# Define the Employee class
class Employee:
    # Constructor to initialize attributes
    def __init__(self):
        self.name = "Taniya"             # Public attribute
        self._designation = "SDE-1"      # Protected attribute (by convention)
        self.__salary = 40000            # Private attribute (name mangled)

    # Method to display employee details
    def show(self):
        print("Name : ", self.name)                  # Accessing public attribute
        print("Designation : ", self._designation)   # Accessing protected attribute
        print("Salary : ", self.__salary)            # Accessing private attribute within the class
emp1=Employee()
# pulic --> can be accessed
print("Name =",emp1.name)
# protected -->should not be accessed outside the class or subclass
print("Designation =",emp1._designation)
# private -->not be accessible with same name,accessible using mangaled name(class.subclass)
print("Salary =",emp1._Employee__salary)

# Output
# Name = Taniya
# Designation = SDE-1
# Salary = 40000 
