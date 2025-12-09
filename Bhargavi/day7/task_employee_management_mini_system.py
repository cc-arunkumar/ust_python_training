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
    
    # Method to calculate yearly salary
    def calculate_yearly_salary(self):
        return self.salary * 12
    
    # Method to apply bonus based on department rules
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
# ------------------- Testing -------------------
emp1 = Employee(101, "Bhargavi", "IT", 50000)

# Show employee info
emp1.show_info()

# Calculate yearly salary
print("Yearly Salary:", emp1.calculate_yearly_salary())

# Apply bonus and show updated salary
bonus = emp1.apply_bonus()
print(f"Bonus Applied: ₹{bonus}")
print("Updated Monthly Salary:", emp1.salary)

#output
# Employee ID: 101
# Name: Bhargavi        
# Department: IT        
# Monthly Salary: ₹50000
# Yearly Salary: 600000
# Bonus Applied: ₹5000.0
# Updated Monthly Salary: 55000.0