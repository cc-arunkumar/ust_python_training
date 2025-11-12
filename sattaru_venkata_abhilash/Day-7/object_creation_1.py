# Define a class to represent an employee
class emp:
    # Initialize employee details
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Promote employee by increasing salary
    def promote(self, increment):
        self.salary += increment
        print(f"{self.name} has been promoted! New salary is {self.salary}")

# Create two employee objects
emp1 = emp("Abhi", 30, 50000000)
emp2 = emp("Meena", 29, 6000000000)

# Display details of first employee
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")

# Display details of second employee
print(f"Employee Name: {emp2.name}")
print(f"Employee Age: {emp2.age}")
print(f"Employee Salary: {emp2.salary}")

# Promote the first employee
emp1.promote(500000)


# Sample Output:
# Employee Name: Abhi
# Employee Age: 30
# Employee Salary: 50000000
# Employee Name: Meena
# Employee Age: 29
# Employee Salary: 6000000000
# Abhi has been promoted! New salary is 50500000
