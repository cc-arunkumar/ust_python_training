# Encapsulation
class Employee:
    def __init__(self):
        self.name="nani"
        self._designation="SDE-1"
        self.__salary=50000

    def show_employee_details(self):
        # no underscore is public
        print("name: ",self.name)
        # single underscore is protected
        print("Designation: ",self._designation)  
        # double underscore is private      
        print("salary: ",self.__salary)
c1=Employee()
print("name: ",c1.name)
print("Designation :",c1._designation)
# this is private but accessed using name mangling (_className__varName)
print("salary: ",c1._Employee__salary)



# output
# name:  nani
# Designation : SDE-1
# salary:  50000
