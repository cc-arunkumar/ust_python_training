#Encapsulation

class Employee:
    def __init__(self):
        #public --> No Restriction
        self.name = "Shakeel"
        #protected with single _ before variable name
        self._designation="SDE-1"
        #private with 2 __ before variable name
        self.__salary=50000

    def show_employee_details_within_same_class(self):
        print("Name :",self.name)
        print("Designation :",self._designation)
        print("Salary :",self.__salary)
emp1=Employee()
print(emp1.__dict__)
print("Name =",emp1.name)
print("Designation = ",emp1._designation)
print("Salary =",emp1._Employee__salary)
        