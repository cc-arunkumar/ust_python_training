#Task : Object Creation

#Code
class Emp:
    def __init__(self, name, age , salary):
        self.name=name
        self.age=age
        self.salary=salary
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} has been promoted ! New salary is {self.salary}")
emp1=Emp("Sohan",22,90000)
emp2=Emp("Sovan",24,890000)
print(f"Employeee name : {emp1.name}")
print(f"Employeee age : {emp1.age}")
print(f"Employeee salary : {emp1.salary}")
print(f"Employee name : {emp2.name}")
print(f"Employeee age : {emp2.age}")
print(f"Employeee salary : {emp2.salary}")

#Output
# Employeee name : Sohan
# Employeee age : 22
# Employeee salary : 90000
# Employee name : Sovan
# Employeee age : 24
# Employeee salary : 890000