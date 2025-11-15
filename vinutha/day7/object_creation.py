# Creating an Object
# Define Emp class
class Emp:
    def __init__(self, name, age, salary):
        # Initialize employee attributes
        self.name = name      # Employee's name
        self.age = age        # Employee's age
        self.salary = salary  # Employee's current salary

    def promote(self, increment):
        # Increase salary by the given increment
        self.salary += increment
        # Display promotion message with updated salary
        print(f"{self.name} has been promoted! New Salary is {self.salary}")


# Create employee objects
emp1 = Emp("Amit", 30, 50000)   # Employee Amit with age 30 and salary 50,000
emp2 = Emp("Sonia", 28, 60000)  # Employee Sonia with age 28 and salary 60,000

# Display details of emp1
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")

# Display details of emp2
print(f"Employee Name: {emp2.name}")
print(f"Employee Age: {emp2.age}")
print(f"Employee Salary: {emp2.salary}")
            

#sample output
# Employee Name:Amit
# Employee Age:30     
# Eployee salary:50000
# Employee Name:Sonia 
# Employee Age:28     
# Eployee salary:60000