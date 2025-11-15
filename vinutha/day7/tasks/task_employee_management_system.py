# Employee Management Mini
# System
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

# Define Employee class
class Employee:
    def __init__(self, emp_id, name, department, salary):
        # Initialize employee attributes
        self.emp_id = emp_id          # Unique ID for the employee
        self.name = name              # Employee's name
        self.department = department  # Department where employee works
        self.salary = salary          # Monthly salary of the employee

    def show_info(self):
        # Display employee details
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: Rs.{self.salary}")

    def calculate_yearly_salary(self):
        # Calculate yearly salary (monthly salary × 12)
        return self.salary * 12

    def bonus(self):
        # Define bonus percentages based on department
        bonus_percentage = {
            "IT": 0.10,       # 10% bonus for IT department
            "HR": 0.08,       # 8% bonus for HR department
            "Finance": 0.12   # 12% bonus for Finance department
        }.get(self.department, 0.05)  # Default 5% bonus for other departments

        # Calculate bonus amount (monthly salary + bonus percentage applied)
        bonus_amount = self.salary * (1 + bonus_percentage)

        # Return both the bonus-applied salary and the percentage used
        return bonus_amount, bonus_percentage


# Create Employee objects
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Perform Operations
employees = [emp1, emp2, emp3]

for emp in employees:
    emp.show_info()
    yearly_salary = emp.calculate_yearly_salary()
    bonus_salary, bonus_percent = emp.bonus()
    print(f"Yearly Salary: Rs.{yearly_salary}")
    print(f"Bonus Applied ({int(bonus_percent * 100)}%): Rs.{int(bonus_salary)}")
    print("*******************************************")

# #output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day7/task1_employee_management_system.py
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.82500
# ---------------------------------------
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: Rs.68000
# ---------------------------------------
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.89600
# ---------------------------------------
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day7/task1_employee_management_system.py
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.82500
# *******************************************
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: Rs.68000
# *******************************************
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.89600
# *******************************************
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day7/task1_employee_management_system.py
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.82500
# *******************************************
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: Rs.68000
# Yearly Salary: Rs.816000
# Bonus Applied (8%): Rs.73440
# *******************************************
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.89600
# *******************************************
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7>