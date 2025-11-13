class Employee:
    def __init__(self):
        #public--> Not restriction
        self.name="Sovan"
        #protected --> Convection: Should not be accessed outside the class or subclass
        self._designation="SDE-1"
        #private--> Name Mangling: cannot be accessed directly outside the class
        self.__salary=500000
        
    def show_employee_details_within_same_class(self):
        print("Name: ",self.name)
        print("Designation: ",self._designation)
        print("Salary: ",self.__salary)
emp1=Employee()
print("Name: ",emp1.name)
print("Designation: ",emp1._designation)
print("Salary: ",emp1._Employee__salary)

#Sample Execution
# Name:  Sovan
# Designation:  SDE-1
# Salary:  500000