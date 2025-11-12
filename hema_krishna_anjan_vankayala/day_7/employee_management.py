# Employee Management Mini System

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
    
# Technical Requirements:

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

# Expected Output Example (cleanly formatted)
# Employee Management Mini System
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: ₹75000
# Yearly Salary: ₹900000
# Bonus Applied (10%): ₹82500
# ---------------------------------------
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: ₹68000
# Yearly Salary: ₹816000
# Bonus Applied (8%): ₹73440
# ---------------------------------------
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: ₹80000
# Yearly Salary: ₹960000
# Bonus Applied (12%): ₹89600
# ---------------------------------------


class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id = emp_id 
        self.name = name 
        self.department = department
        self.salary = salary 
    
    def show_info(self):
        print(f"Employee ID: {self.emp_id}\n Name: {self.name}\n Department: {self.department}")
        print(f"Monthly Salary: Rs.{self.salary}")

    def calcualte_yearly_salary(self):
                print("Yearly Salary: Rs.",self.salary*12)
    
    def apply_bonus(self):
        if self.department=="IT":
            self.salary += self.salary * 0.1
            print(f"Bonus Applied (10%) :{self.salary}\n")

        elif self.department == "HR":
            self.salary += self.salary * (8/100)
            print(f"Bonus Applied (8%) :{self.salary}")

        elif self.department=="Finance":
            self.salary += self.salary * (12/100)
            print(f"Bonus Applied (12%) :{self.salary}")

        else:
            self.salary += self.salary * (5/100)
            print(f"Bonus Applied (5%) :{self.salary}")

        

emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

emp1.show_info()
emp1.calcualte_yearly_salary()
emp1.apply_bonus()

emp2.show_info()
emp2.calcualte_yearly_salary()
emp2.apply_bonus()

emp3.show_info()
emp3.calcualte_yearly_salary()
emp3.apply_bonus()


#Sample Output:
    # Employee ID: 101
    #  Name: Arun Kumar
    #  Department: IT
    # Monthly Salary: Rs.75000
    # Yearly Salary: Rs. 900000
    # Bonus Applied (10%) :82500.0
    
    # Employee ID: 102
    #  Name: Riya Sharma
    #  Department: HR
    # Monthly Salary: Rs.68000
    # Yearly Salary: Rs. 816000
    # Bonus Applied (8%) :73440.0
    
    # Employee ID: 103
    #  Name: John Doe
    #  Department: Finance
    # Monthly Salary: Rs.80000
    # Yearly Salary: Rs. 960000
    # Bonus Applied (12%) :89600.0