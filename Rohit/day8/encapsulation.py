class Employee:
    def __init__(self):
        # Public attribute (accessible anywhere)
        self.name = "Rohit"
        # Protected attribute (accessible, but by convention should not be used outside the class)
        self._designation = "SDE-1"
        # Private attribute (hidden via name mangling)
        self.__salary = 50000
       
    def show_employee_details_within_same_class(self):
        # Accessing all attributes inside the same class works fine
        print("Name: ", self.name)
        print("designation: ", self._designation)
        print("salary : ", self.__salary)


# Create an Employee object
emp1 = Employee()

# Access public attribute directly
print("Name: ", emp1.name)

# Access protected attribute directly (possible but not recommended)
print("Designation : ", emp1._designation)

# Access private attribute using name mangling (_ClassName__attribute)
print("Salary: ", emp1._Employee__salary)


# ==================sample output===================
# Name:  Rohit
# Designation :  SDE-1
# Salary:  50000
