# Creating class
class Emp:
    # Creaing constructor
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def promote(self,increment):
        self.salary += increment
        print(f"{self.name} has bees promoted! New salary is {self.salary}")
        
# Creating objects of the Emp class
emp1 = Emp("Arjun",35,50000)
emp2 = Emp("Akhil",30,60000)

# Displaying details
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")
print(f"Employee Name: {emp2.name}")
print(f"Employee Age: {emp2.age}")
print(f"Employee Salary: {emp2.salary}")

emp1.promote(5000)
emp2.promote(3000)

# output

# Employee Name: Arjun
# Employee Age: 35
# Employee Salary: 50000
# Employee Name: Akhil
# Employee Age: 30
# Employee Salary: 60000
# Arjun has bees promoted! New salary is 55000
# Akhil has bees promoted! New salary is 63000