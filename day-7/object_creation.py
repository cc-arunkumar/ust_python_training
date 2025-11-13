class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} has promoted! Now salary is{self.salary}")

emp1=Emp("amit",30,50000)
emp2=Emp("lara",28,60000) 

print(f"Employee Name:{emp1.name}") 
print(f"Employee Age:{emp1.age}") 
print(f"Employee Salary:{emp1.salary}") 
print(f"Employee Name:{emp2.name}") 
print(f"Employee Age:{emp2.age}") 
print(f"Employee Salary:{emp2.salary}")     


#o/p:
# Employee Name:amit
# Employee Age:30
# Employee Salary:50000
# Employee Name:lara
# Employee Age:28
# Employee Salary:60000         