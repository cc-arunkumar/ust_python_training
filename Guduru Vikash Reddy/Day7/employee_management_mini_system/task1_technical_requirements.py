# Objective:
# Learn how to define a class, create multiple objects, and interact with them — just
# like how HR systems track employees in a company.
# Scenario:
# UST wants to build a very simple internal HR module in Python to store employee
# data temporarily and calculate key details.
# Each Employee should have:
# emp_id
# name
# department
# salary
# and should be able to:
# Display personal details
# Calculate yearly salary
# Apply a bonus based on department
# Technical Requirements
# Step 1: Create a class Employee with:
# Attribute Description
# emp_id Unique employee number
# name Full name of employee
# Employee Management Mini System 1
# Attribute Description
# department e.g. IT, HR, Finance, Marketing
# salary Monthly salary
# Step 2: Add Methods
# Method Description
# show_info() Prints all details of the employee in a clean format
# calculate_yearly_salary() Returns yearly salary ( salary * 12 )
# apply_bonus() Adds bonus to salary based on department (rules below)
# Bonus rules:
# IT → 10% bonus
# HR → 8% bonus
# Finance → 12% bonus
# Others → 5% bonus
# Step 3: Create at least 3 Employee objects manually:
# emp1 = Employee(101, "Arun Kumar", "IT", 75000)
# emp2 = Employee(102, "Riya Sharma", "HR", 68000)
# emp3 = Employee(103, "John Doe", "Finance", 80000)
# Step 4: Perform Operations
# 1. Print details of each employee using show_info() .
# 2. Show each employee’s yearly salary.
# 3. Apply a bonus using apply_bonus() and display the updated salary.
# Step 1: Define the Employee class with basic attributes
class Employee:
    
    # Step 2: Initialize employee details (ID, name, department, salary)
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    # Step 3: Display employee information
    def show_info(self):
        print(f"Employee ID:", self.emp_id)
        print(f"Name:", self.name)
        print(f"Department:", self.department)

    # Step 4: Calculate and display monthly and yearly salary
    def calculate_yearly_salary(self):
        yearly_salary = self.salary * 12
        print(f"Monthly salary:", yearly_salary / 12)
        print(f"Yearly salary:", yearly_salary)

    # Step 5: Apply department-specific bonus to salary
    def apply_bonus(self):
        if self.department == "IT":
            self.salary += self.salary * 0.10
            print(f"Bonus Applied (10%):", self.salary)
        elif self.department == "HR":
            self.salary += self.salary * 0.08
            print(f"Bonus Applied (8%):", self.salary)
        elif self.department == "Finance":
            self.salary += self.salary * 0.12
            print(f"Bonus Applied (12%):", self.salary)
        else:
            self.salary += self.salary * 0.05
            print(f"Bonus Applied (5%):", self.salary)

# Step 6: Create employee objects and invoke their methods
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

emp1.show_info()
emp1.calculate_yearly_salary()
emp1.apply_bonus()

emp2.show_info()
emp2.calculate_yearly_salary()
emp2.apply_bonus()

emp3.show_info()
emp3.calculate_yearly_salary()
emp3.apply_bonus()

# sample output
# Employee ID: 101
# Name: Arun Kumar
# Department:  IT
# montly salary: 75000.0     
# yearly salary: 900000      
# Bonus Applied (10%) 82500.0
# Employee ID: 102
# Name: Riya Sharma
# Department:  HR
# montly salary: 68000.0     
# yearly salary: 816000
# Bonus Applied (8%) 73440.0
# Employee ID: 103
# Name: John Doe
# Department:  Finance
# montly salary: 80000.0
# yearly salary: 960000
# Bonus Applied (12%) 89600.0