
#Creating a class name Emp and promoting with increment  
class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} ha been promoted! New salary is{self.salary}")
        
emp1=Emp("Amit",45,30000)
emp2=Emp("Arjun",67,67000)

#Displaying the initial details

print(f"Employee1 name:{emp1.name}")
print(f"Employee1 age:{emp1.age}")
print(f"Employee1 salary:{emp1.salary}")
print(f"Employee2 name:{emp2.name}")
print(f"Employee2 age:{emp2.age}")
print(f"Employee salary:{emp2.salary}")
emp1.promote(20000)
emp2.promote(10000)

# sample execution
# Employee1 name:Amit
# Employee1 age:45
# Employee1 salary:30000
# Employee2 name:Arjun
# Employee2 age:67
# Employee salary:67000
# Amit ha been promoted! New salary is50000
# Arjun ha been promoted! New salary is77000