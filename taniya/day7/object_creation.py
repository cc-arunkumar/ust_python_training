# Define a class Emp to represent an employee
class Emp:
    # Constructor to initialize employee attributes
    def __init__(self, name, age, salary):
        self.name = name      # Employee's name
        self.age = age        # Employee's age
        self.salary = salary  # Employee's salary
    
    # Method to promote employee by increasing salary
    def promote(self, promotion):
        # Increase salary by 5% of the promotion amount
        self.salary += promotion * 0.05
        # Print updated salary after promotion
        print(f"{self.name} has been promoted! New salary is {self.salary}")


# Create first employee object
emp1 = Emp("Amit", 22, 50000)

# Create second employee object
emp2 = Emp("Sonia", 24, 60000)


# Print details of emp1
print(f"Employee Name: {emp1.name}")    # Output employee name
print(f"Employee Name: {emp1.age}")     # Output employee age
print(f"Employee Name: {emp1.salary}")  # Output employee salary

# Print details of emp2
print(f"Employee Name: {emp2.name}")    # Output employee name
print(f"Employee Name: {emp2.age}")     # Output employee age
print(f"Employee Name: {emp2.salary}")  # Output employee salary


# Promote emp1 with a promotion value of 50000
emp1.promote(50000)


# -------------------------------
# Expected Output
# -------------------------------
# Employee Name: Amit
# Employee Name: 22
# Employee Name: 50000
# Employee Name: Sonia
# Employee Name: 24
# Employee Name: 60000
# Amit has been promoted! New salary is 52500.0