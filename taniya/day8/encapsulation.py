class Employee:
    def __init__(self):
        self.name="Taniya"
        self._designation="SDE-1"
        self.__salary= 40000
    
    def show(self):
        print("Name : ",self.name)
        print("Designation : ",self._designation)
        print("Salary : ",self.__salary)
        
emp1=Employee()
# pulic --> can be accessed
print("Name =",emp1.name)
# protected -->should not be accessed outside the class or subclass
print("Designation =",emp1._designation)
# private -->not be accessible with same name,accessible using mangaled name(class.subclass)
print("Salary =",emp1._Employee__salary)
