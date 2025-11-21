# Employee class to store basic details and handle salary update
class Employee:
    def __init__(self, name, age, salary):
        self.name = name      # Employee name
        self.age = age        # Employee age
        self.salary = salary  # Employee salary
    
    # Method to increase salary by given increment amount
    def promotion(self, increment):
        self.salary += increment
        print(f"Salary incremented Rs.{increment} for {self.name}")


# Taking user input for employee details
name = input("Enter Employee Name: ")
age = int(input("Enter Employee age: "))
salary = int(input("Enter Employee Salary: "))

# Creating Employee object with user inputs
emp1 = Employee(name, age, salary)

# Displaying employee  details
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")


"""
SAMPLE OUTPUT
Enter Employee Name: Gowtham
ENter Employee age: 21
Enter Employee Salary: 30000
Employee Name:Gowtham
Employee age:21
Employee Salary:30000
"""