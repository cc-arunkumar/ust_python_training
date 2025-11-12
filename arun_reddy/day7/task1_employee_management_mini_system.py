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
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: ₹75000
# Yearly Salary: ₹900000
# Bonus Applied (10%): ₹82500


class Employee:
    # intilaing the contructor wit the valkues given 
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary 
        
        
    def show_info(self):
        # printing the info of employeee
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Montly Salary: {self.salary}")
        
        #calculation of the yearly salary
    def calculate_yearly_salary(self):
        return self.salary*12
    
    
# apply_bonus() Adds bonus to salary based on department (rules below)
# Bonus rules:
# IT → 10% bonus
# HR → 8% bonus
# Finance → 12% bonus
# Others → 5% bonus
    def  apply_bonus(self):
        match self.department:
            case "IT":
                self.salary+=int(self.salary*0.10)
                print(f"Bonus applied(10%) :{self.salary}")
            case "HR":
                self.salary+=int(self.salary*0.10)
                print(f"Bonus applied(10%) :{self.salary}")
            case "Finance":
                self.salary+=int(self.salary*0.12)
                print(f"Bonus applied(12%) {self.salary}")
            case _:
                self.salary+=int(self.salary*0.05)
                print("Bonus applied(5%) {self.salary}")
                
                
        
# Step 3: Create at least 3 Employee objects manually:
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Step 4: Perform Operations
# 1. Print details of each employee using show_info() .
# 2. Show each employee’s yearly salary.
# 3. Apply a bonus using apply_bonus() and display the updated salary.
emp1.show_info()
print(f"Yearly salary :{emp1.calculate_yearly_salary()}")
emp1.apply_bonus()
print("=====================================================")
emp2.show_info()
print(f"Yearly salary :{emp2.calculate_yearly_salary()}")
emp2.apply_bonus()
print("=====================================================")
emp3.show_info()
print(f"Yearly salary :{emp3.calculate_yearly_salary()}")
emp3.apply_bonus()
print("=====================================================")




### sample execution
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Montly Salary: 75000
# Yearly salary :900000
# Bonus applied(10%) :82500
# =====================================================
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Montly Salary: 68000
# Yearly salary :816000
# Bonus applied(8%) 73440
# =====================================================
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Montly Salary: 80000
# Yearly salary :960000
# Bonus applied(12%) 89600 