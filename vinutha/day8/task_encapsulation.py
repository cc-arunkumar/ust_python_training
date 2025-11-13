# Encapsulation
class Employee:
    def __init__(self):
        #public->no restriction
        self.name="Vinnu"
        # Protected 
        self._designation="SDE-1"
        # private
        self.__salary=50000
    def show_details(self):
        print("Name:",self.name)
        print("Designation:",self._designation)
        print("Salary:",self.__salary)
emp1=Employee()
# print(emp1.__dict__)
print("Name:",emp1.name)
print("Designation:",emp1._designation)
# print("Salary:",emp1.__salary) --> we cant access directly
print("Salary:",emp1._Employee__salary)

#output
# Name= Vinnu
# Designation: SDE-1
# Salary: 50000
