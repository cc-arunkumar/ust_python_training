# Class definition for Emp
class Emp:
    a = 150000  # Class variable for a fixed value

    # Constructor to initialize employee details
    def __init__(self, name, age, salary):
        self.name = name  # Employee's name
        self.age = age  # Employee's age
        self.salary = salary  # Employee's salary

    # Method to promote an employee by increasing salary
    def promote(self, increment):
        self.salary += increment  # Increase salary by given increment
        print(f"{self.name} has been promoted! New salary is {self.salary}")  # Print promotion message

# Create two employee objects
emp1 = Emp("Deva", 25, 40000)
emp2 = Emp("Raj", 29, 60000)

# Print details of emp1
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")

# Print details of emp2
print(f"Employee Name: {emp2.name}")
print(f"Employee Age: {emp2.age}")
print(f"Employee Salary: {emp2.salary}")

# Promote emp1 and print the new salary
emp1.promote(100000)

# Print the value of class variable 'a'
print(Emp.a)
