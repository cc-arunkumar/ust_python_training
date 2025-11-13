# Access Modifiers

class Employee:
    def __init__(self):
        #public --> No restriction
        self.name="Niranjan"

        # protected --> Convection: should not be accessed outside the class or subclass
        self._designation="trainee"

        # Private --> Name mangling: cannot be accessed directly outside the class
        self.__salary=35000

    def show_details_within_same_class(self):
        print("Name:",self.name)    
        print("Designation:",self._designation)
        print("Salary:",self.__salary)

emp1=Employee()
# print(emp1.__dict__)

print("Name:",emp1.name)    
print("Designation:",emp1._designation)
# print("Salary:",emp1.__salary)       #Not accessible with same name, accessible using mangled name(_ClassName__varName)
print("Salary:",emp1._Employee__salary)

# Sample output

# Name: Niranjan
# Designation: trainee
# Salary: 35000