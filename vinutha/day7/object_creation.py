# Creating an Object

class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name}has been promoted!New Salary is{self.salary}")
emp1=Emp("Amit",30,50000)
emp2=Emp("Sonia",28,60000)

print(f"Employee Name:{emp1.name}")
print(f"Employee Age:{emp1.age}")
print(f"Eployee salary:{emp1.salary}") 
print(f"Employee Name:{emp2.name}")
print(f"Employee Age:{emp2.age}")
print(f"Eployee salary:{emp2.salary}")               

#sample output
# Employee Name:Amit
# Employee Age:30     
# Eployee salary:50000
# Employee Name:Sonia 
# Employee Age:28     
# Eployee salary:60000