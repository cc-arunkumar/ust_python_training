# Employee Management Mini System
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
# 3. Apply a bonus using apply_bonus() and display the updated salar

class emp:
    def __init__(self,emp_id,name,dept,salary):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary

    def show_info(self):
        print(f"employee id:{self.emp_id}")
        print(f"employee name: {self.name}")
        print(f"employee dept: {self.dept}")
        
    def calculate_yearly_sal(self):
        yearly_salary=self.salary*12
        # calculating the yearly_salary
        print(f"employee yearly salary: {yearly_salary}")
        print(f"monthly salary: {yearly_salary/12}")

        # using if loop and calculating the bonus
    def bonus(self):
        if self.dept=="IT":
            self.salary+=self.salary*0.1
            print(f"employee bonus(10%): {self.salary}")
        elif self.dept=="HR":
            self.salary+=self.salary*0.08
            print(f"employee bonus(8%): {self.salary}")
        elif self.dept=="Finance":
            self.salary+=self.salary*0.12
            print(f"employee bonus(12%): {self.salary}")
        else:
            self.salary+=self.salary*0.05
            print(f"employee bonus(5%): {self.salary}")
    


emp1=emp(101, "Arun Kumar", "IT", 75000)
emp2=emp(102, "Riya Sharma", "HR", 68000)
emp3=emp(103, "John Doe", "Finance", 80000)

emp1.show_info()
emp1.calculate_yearly_sal()
emp1.bonus()

emp2.show_info()
emp1.calculate_yearly_sal()
emp1.bonus()
emp3.show_info()
emp3.calculate_yearly_sal()
emp3.bonus()

# output
# employee id:101
# employee name: Arun Kumar
# employee dept: IT
# employee yearly salary: 900000
# monthly salary: 75000.0
# employee bonus(10%): 82500.0
# employee id:102
# employee name: Riya Sharma
# employee dept: HR
# employee yearly salary: 990000.0
# monthly salary: 82500.0
# employee bonus(10%): 90750.0
# employee id:103
# employee name: John Doe
# employee dept: Finance
# employee yearly salary: 960000
# monthly salary: 80000.0
# employee bonus(12%): 89600.0