#Implementing encapsulation 

class Employee:
    def __init__(self):
        
        #public=no restriction
        self.name="Yashu"
        
        #protected=convention: should not be accessed outside the class or subclass
        self._designation="SDE-1"
        
        #private=Name Mangling: cannot be accessed directly outside the class
        self.__salary=50000
        
    def show_employee_details_within_same_class(self):
        print("Name:",self.name)
        print("Designation:",self.__designation)
        print("Salary:",self.__salary)
        
emp1=Employee()
#print(emp1.__dict__)
print("Name:",emp1.name)
print("Designation:",emp1._designation)      #shouldn't be accessed
print("Salary:",emp1._Employee__salary)      #not accessible with same class,

#o/p:
# Name: Yashu
# Designation: SDE-1
# Salary: 50000