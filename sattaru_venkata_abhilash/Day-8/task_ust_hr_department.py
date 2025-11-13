class Employee:
    def __init__(self):
        # Public attribute
        self.name = "Abhi"
        
        # Protected attribute (convention: should not be accessed directly outside class)
        self._designation = "CEO"
        
        # Private attribute (Name Mangling: becomes _Employee__salary internally)
        self.__salary = "600000000"

    # Getter method to access private salary
    def get_salary(self):
        # Accessing private variable using name-mangled form
        print("Employees Salary: ", self._Employee__salary)

    # Setter method to update private salary
    def set_salary(self, amount):
        if amount > 0:
            # Updating private salary using name-mangled variable
            self._Employee__salary = amount    
            print("Updating salary : ", self._Employee__salary)

    # Method to show all info
    def show_info(self):
        print("Name : ", self.name)
        print("Designation: ", self._designation)
        # Accessing private salary normally inside the class
        print("salary: ", self.__salary)


# Creating object
emp1 = Employee()

# Accessing public attribute
print("Name = ", emp1.name)

# Accessing protected attribute (not recommended in real applications)
print("Designation = ", emp1._designation)

# Accessing private attribute directly will cause an error
print("Trying to access private salary directly -> AttributeError: 'Employee' object has no attribute '__salary'.")

# Accessing private variable using name mangling
print("Salary = ", emp1._Employee__salary)

# Calling getter method
emp1.get_salary()


# sample output:
# Name =  Abhi
# Designation =  CEO
# Trying to access private salary directly -> AttributeError: 'Employee' object has no attribute '__salary'.
# Salary =  600000000
# Employees Salary:  600000000
