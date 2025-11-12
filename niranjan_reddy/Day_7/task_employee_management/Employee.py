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
# Apply a bonus based on departmen


# Step 1: Create a class Employee with:
# Attribute Description
# emp_id-Unique employee number
# name- Full name of employee
# department- e.g. IT, HR, Finance, Marketing
# salary- Monthly salary

class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id= emp_id
        self.name= name
        self.department= department
        self.salary= salary 


    # Step 2: Add Methods
    # Method Description
    # show_info() Prints all details of the employee in a clean format
    
    def show_info(self):
        print(f"Employee Id: {self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee department:{self.department}")
        print(f"Employee Salary: ₹{self.salary}")

    # calculate_yearly_salary() Returns yearly salary ( salary * 12 )

    def calculate_yearly_salary(self):
        yearly=self.salary*12
        print(f"Yearly Salary: ₹{yearly}")



    # apply_bonus() Adds bonus to salary based on department (rules below)
    def apply_bonus(self):
        if self.department=="IT":
            self.salary+=int(self.salary*0.1)
            print(f"Bonus Applied (10%) : ₹{self.salary}")

        elif self.department=="HR":
            self.salary+=int(self.salary*0.08)
            print(f"Bonus Applied (8%) : ₹{self.salary}")
        
        elif self.department=="Finance":
            self.salary+=int(self.salary*0.12)
            print(f"Bonus Applied (12%) : ₹{self.salary}")
        
        else:
            self.salary+=int(self.salary*0.05)
            print(f"Bonus Applied (5%) : ₹{self.salary}")
        
        

# Step 3: Create at least 3 Employee objects manually
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)


# Step 4: Perform Operations
# 1. Print details of each employee using show_info() .
# 2. Show each employee’s yearly salary.
# 3. Apply a bonus using apply_bonus() and display the updated salary.

emp1.show_info()
emp1.calculate_yearly_salary()
emp1.apply_bonus()

print("---------------------------------------")

emp2.show_info()
emp2.calculate_yearly_salary()
emp2.apply_bonus()

print("---------------------------------------")
emp3.show_info()
emp3.calculate_yearly_salary()
emp3.apply_bonus()


# Sample output

# Employee Id: 101
# Employee Name:Arun Kumar
# Employee department:IT
# Employee Salary: ₹75000
# Yearly Salary: ₹900000
# Bonus Applied (10%) : ₹82500
# ---------------------------------------
# Employee Id: 102
# Employee Name:Riya Sharma
# Employee department:HR
# Employee Salary: ₹68000
# Yearly Salary: ₹816000
# Bonus Applied (8%) : ₹73440
# ---------------------------------------
# Employee Id: 103
# Employee Name:John Doe
# Employee department:Finance
# Employee Salary: ₹80000
# Yearly Salary: ₹960000
# Bonus Applied (12%) : ₹89600
