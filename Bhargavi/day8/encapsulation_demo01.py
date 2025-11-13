#Modifiers in encapsulation

class Employee:
    def __init__(self):
        self.name = "Bhargavi S"  #public = can accesible anywhere no restrictions
        self._designation = "SDE-1" #protected - for the convention we should not be accessed outside the class or subclass
        self.__salary = 50000  #private can be accesed by name mangling
        
    def show_employee_details_within_same_class(self):
        print("Name :" , self.name)
        print("Designation :", self._designation)
        print("salary : " , self.__salary)
        
emp1 = Employee()
print("Name = ", emp1.name)
print("Designation :" , emp1._designation)
print("salary :" , emp1._Employee__salary)

#output
# Name =  Bhargavi S
# Designation : SDE-1
# salary : 50000