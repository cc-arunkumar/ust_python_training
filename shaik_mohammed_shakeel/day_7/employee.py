class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} has been promoted, New salary is{self.salary}")

#creating object for Emp class
emp1=Emp("Amit",30,50000)
emp2=Emp("Rahul",22,35000)

#displaying initial details

print(f"Employee Name: {emp1.name}")
print(f"Employee Name: {emp1.age}")
print(f"Employee Name: {emp1.salary}")
print(f"Employee Name: {emp2.name}")
print(f"Employee Name: {emp2.age}")
print(f"Employee Name: {emp2.salary}")