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
class Employee:
    
    # Step 1: Create a class Employee with:
    # Attribute Description
    # emp_id Unique employee number
    # name Full name of employee
    # Employee Management Mini System 1
    # Attribute Description
    # department e.g. IT, HR, Finance, Marketing
    # salary Monthly 
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
        
    #Step 2: Add Methods
    # Method Description
    # show_info() Prints all details of the employee in a clean format
    # calculate_yearly_salary() Returns yearly salary ( salary * 12 )
    # apply_bonus() Adds bonus to salary based on department (rules below)
    # Bonus rules:
    # IT → 10% bonus
    # HR → 8% bonus
    # Finance → 12% bonus
    # Others → 5% bonus
    def show_info(self):
        print("Employee ID: ",self.emp_id)
        print("Name: ",self.name)
        print("Department: ",self.department)
        print("Monthly salary: ₹",self.salary)
    
    def calculate_yearly_salary(self):
        print("Yearly salary : ₹",self.salary*12)
    
    def apply_bonus(self):
        dep=self.department
        if dep=="IT":
            self.salary+=(self.salary*0.10)
            print("Bonus Applied (10%): ₹",self.salary)
        elif dep=="HR":
            self.salary+=(self.salary*0.08)
            print("Bonus Applied (8%): ₹",self.salary)
        elif dep=="Finance":
            self.salary+=(self.salary*0.12)
            print("Bonus Applied (12%): ₹",self.salary)
        else:
            self.salary+=(self.salary*0.05)
            print("Bonus Applied (8%): ₹",self.salary)

# Step 3: Create at least 3 Employee objects manually
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Step 4: Perform Operations
# 1. Print details of each employee using show_info() .
# 2. Show each employee’s yearly salary.
# 3. Apply a bonus using apply_bonus() and display the updated salary.
employees_data=[emp1,emp2,emp3]
for emp in employees_data:
    emp.show_info()
    emp.calculate_yearly_salary()
    emp.apply_bonus()
    print("---------------------------")
    
# emp1.show_info()
# emp1.calculate_yearly_salary()
# emp1.apply_bonus()
# print("---------------------------")


# emp2.show_info()
# emp2.calculate_yearly_salary()
# emp2.apply_bonus()
# print("---------------------------")


# emp3.show_info()
# emp3.calculate_yearly_salary()
# emp3.apply_bonus()
# print("---------------------------")

# Sampel output
# Employee ID:  101
# Name:  Arun Kumar
# Department:  IT
# Monthly salary: ₹ 75000
# Yearly salary : ₹ 900000
# Bonus Applied (10%): ₹ 82500.0
# ---------------------------
# Employee ID:  102
# Name:  Riya Sharma
# Department:  HR
# Monthly salary: ₹ 68000
# Yearly salary : ₹ 816000
# Bonus Applied (8%): ₹ 73440.0
# ---------------------------
# Employee ID:  103
# Name:  John Doe
# Department:  Finance
# Monthly salary: ₹ 80000
# Yearly salary : ₹ 960000
# Bonus Applied (12%): ₹ 89600.0
# ---------------------------