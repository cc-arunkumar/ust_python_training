class Emp:
    def __init__(self, name, age, salary): 
        self.name = name
        self.age = age
        self.salary = salary

    def promote(self, increment):
        self.salary += increment
        print(f"{self.name} has been promoted! New salary is {self.salary}")


emp1 = Emp("Amit", 30, 500000)
emp2 = Emp("Sonia", 28, 60000)

print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")
print(f"Employee Name: {emp2.name}")
print(f"Employee Age: {emp2.age}")
print(f"Employee Salary: {emp2.salary}")


    