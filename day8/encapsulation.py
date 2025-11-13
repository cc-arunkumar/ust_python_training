# Encapsulation demonstration

class Employee:
    def __init__(self):
        
# public --> with no restrictions
        self.name="Varsha"
# protected --> convention should not be accessed outside the class or subclass
        self._designation="SDE 1"
# private --> 
        self.__salary=500000

    def show_employee_details_within_same_class(self):
        print("Name : ",self.name)
        print("Designation :",self._designation)
        print("Salary : ",self.__salary)

emp1=Employee()
print("Name = ",emp1.name)
print("Designation = ",emp1._designation)
print("salary = ",emp1._Employee__salary,"yes")

    

# Output
# Name =  Varsha
# Designation =  SDE 1
# salary =  500000 yes



