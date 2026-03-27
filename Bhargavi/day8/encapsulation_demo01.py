#Modifiers in encapsulation

# This statement outputs the designation of the employee or object by accessing its _designation attribute. It helps display the role/title assigned to the instance in a clear, readable format.

class Employee:
    #constructor intisializing the variours type of variables with modifers
    def __init__(self):
        self.name = "Bhargavi S"  #public = can accesible anywhere no restrictions
        self._designation = "SDE-1" #protected - for the convention we should not be accessed outside the class or subclass
        self.__salary = 50000  #private can be accesed by name mangling
        
    # Method to show employee details within the same class
    def show_employee_details_within_same_class(self):
        print("Name :" , self.name)
        print("Designation :", self._designation)
        print("salary : " , self.__salary)
        
# Creating object of Employee class
emp1 = Employee()
print("Name = ", emp1.name)
print("Designation :" , emp1._designation)
print("salary :" , emp1._Employee__salary)

#output
# Name =  Bhargavi S
# Designation : SDE-1
# salary : 50000