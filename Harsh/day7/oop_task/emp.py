class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def promote(self,inc):
        self.salary+=inc
        print(f"{self.name} has been promoted! New salary is {self.salary}")

emp1=Emp("Harsh",22,60000)
emp2=Emp("Rohit",22,50000)

print(f"Employee name: {emp1.name}")
print(f"Employee age: {emp1.age}")
print(f"Employee salary: {emp1.salary}")
print(f"Employee name: {emp2.name}")
print(f"Employee age: {emp2.age}")
print(f"Employee salary: {emp2.salary}")

emp1.promote(100000)