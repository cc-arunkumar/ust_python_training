class Emp:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def promote(self,promotion):
        self.salary += promotion * 0.05
        print(f"{self.name} has been promoted! New salary is {self.salary}")
    
emp1 = Emp("Amit",22,50000)
emp2 = Emp("Sonia",24,60000)

print(f"Employee Name: {emp1.name}")
print(f"Employee Name: {emp1.age}")
print(f"Employee Name: {emp1.salary}")
print(f"Employee Name: {emp2.name}")
print(f"Employee Name: {emp2.age}")
print(f"Employee Name: {emp2.salary}")

emp1.promote(50000)

