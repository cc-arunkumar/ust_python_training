# Encapsulation

class Employee:
    def __init__(self):
        # public --> No Restrictions
        self.name = "Sai Vamsi"

        # protected --> Convention:should not be accessed outside the class or subclass
        self._designation = "SDE-1"

        # private --> Name mangling: cannot be accessed directly outside the class
        self.__salary = 50000

    def show_employee_details_within_same_class(self):
        print("Name:",self.name)
        print("Designation:",self._designation)
        print("Salary:",self.__salary)

emp1 = Employee()
# print(emp1.__dict__)
print("Name=",emp1.name)

# shouldn't be accessed
print("Designation = ",emp1._designation) 

# print("Salary = " , emp1.salary)             --> Not accessible with same name, accesible
print("Salary = ",emp1._Employee__salary)

# -------------------------------------------------------------------------------------

# Sample Output

# Name= Sai Vamsi
# Designation =  SDE-1
# Salary =  50000