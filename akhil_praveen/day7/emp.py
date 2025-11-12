class Emp:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} has been promoted! New salary is {self.salary}\n")
 
# creating new objects for employees 
emp1 = Emp("Akhil",22,100000)

emp2 = Emp("Arjun",23,100000)

# emp1 promoted
emp1.promote(100000)

# display emp status
print(f"Employee name: {emp1.name}")
print(f"Employee name: {emp1.age}")
print(f"Employee name: {emp1.salary}")
print("")
print(f"Employee name: {emp2.name}")
print(f"Employee name: {emp2.age}")
print(f"Employee name: {emp2.salary}")

# output
# Akhil has been promoted! New salary is 200000

# Employee name: Akhil
# Employee name: 22
# Employee name: 200000

# Employee name: Arjun
# Employee name: 23
# Employee name: 100000