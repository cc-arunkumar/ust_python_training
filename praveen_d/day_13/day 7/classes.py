class Emp:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    
    def promote(self,incerement):
        self.salary+=incerement

    
emp1=Emp("Amit",101,10000)
emp2=Emp("Araiya",102,20000)

# Print employee details
print(f"Name:{emp1.name}")
print(f"Id:{emp1.id}")
print(f"Salary:{emp1.salary}")
print(f"Name:{emp2.name}")
print(f"Id:{emp2.id}")
print(f"Salary:{emp2.salary}")

# Incrementing the salary
emp1.promote(20000)
print(f"salary Incremented")
print(f"Name:{emp1.name}")
print(f"Id:{emp1.id}")
print(f"Salary:{emp1.salary}")


# print(emp1.name)
