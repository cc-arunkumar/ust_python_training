# Employee Management Mini System

# Step 1: Create a class Employee 
# Attribute Description
# emp_id Unique employee number
# name Full name of employee
# Attribute Description
# department e.g. IT, HR, Finance, Marketing
# salary Monthly salary

# Step 1: Create a class Employee 
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


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

# Step 2: Add Methods
    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.salary}")

    def calculate_yearly_salary(self):
        return self.salary * 12

    def apply_bonus(self):
        bonus_percent = 0
        if self.department == "IT":
            bonus_percent = 10
        elif self.department == "HR":
            bonus_percent = 8
        elif self.department == "Finance":
            bonus_percent = 12
        else:
            bonus_percent = 5

        bonus_amount = self.salary * bonus_percent / 100
        self.salary += bonus_amount
        return bonus_amount

# Employee ID: 101
# Name: BhargaviS
# Department: IT
# Monthly Salary: ₹75000    
# Yearly Salary: ₹900000    
# Bonus Applied (10%): ₹7500
# ----------------------------------------
# Employee ID: 102
# Name: Vinutha
# Department: HR
# Monthly Salary: ₹68000
# Yearly Salary: ₹816000
# Bonus Applied (8%): ₹5440
# ----------------------------------------
# Employee ID: 103
# Name: Memma
# Department: Finance
# Monthly Salary: ₹80000
# Yearly Salary: ₹960000
# Bonus Applied (12%): ₹9600
# ----------------------------------------