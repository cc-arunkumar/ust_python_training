# This program defines an Employee class with attributes name, age, and salary.
# It allows salary increments through the promotion() method and displays employee details entered by the user.

# Employee class definition
class Employee:
    def __init__(self, name, age, salary):
        # Initialize employee attributes
        self.name = name
        self.age = age
        self.salary = salary
    
    def promotion(self, increment):
        # Method to increase salary by a given increment
        self.salary += increment
        print(f"Salary incremented Rs.{increment} for {self.name}")


# Taking user input for employee details
name = input("Enter Employee Name: ")
age = int(input("Enter Employee age: "))
salary = int(input("Enter Employee Salary: "))

# Creating Employee object
emp1 = Employee(name, age, salary)

# Displaying employee details
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")


#output
# Enter Employee Name: Bhargavi S
# ENter Employee age: 12
# Enter Employee Salary: 3000
# Employee Name:Bhargavi S
# Employee age:12
# Employee Salary:3000