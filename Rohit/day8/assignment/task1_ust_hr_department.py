class Employee:
    def __init__(self):
       self.name = "Rohit"
       self._designation="SDE-1"
       self.__salary=50000
       
       
    def get_salary(self):
        print(self.__salary)

    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("salary is less than zero not acceptable")
    


emp1=Employee()
print("employee name ",emp1.name)
print("employee designation ",emp1._designation)
emp1.set_salary(75000)
emp1.get_salary()
try:
    print(emp1.__salary)
except AttributeError:
    print("Trying to access private salary directly -> ERROR",AttributeError)
    