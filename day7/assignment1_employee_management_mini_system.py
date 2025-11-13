# Employee Management Mini System
# Create a class Employee with
# emp_id : Unique employee number
# name: Full name of employee
# department :e.g. IT, HR, Finance, Marketing
# salary : Monthly salary


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary

# Add Methods
# show_info()

    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.salary}")
        
# calculate_yearly_salary() 

    def calculate_yearly_salary(self):
        return self.salary*12
    
# apply_bonus()

    def apply_bonus(self):
        bonus_percent=0
        if self.department=="IT":
            bonus_percent=10
        elif self.department=="HR":
            bonus_percent=8
        elif self.department=="Finance":
            bonus_percent=12
        else:
            bonus_percent=5

        bonus_amount=self.salary*bonus_percent/100
        self.salary+=bonus_amount
        return bonus_amount
    
# Step 3: Create employee objects
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Step 4: Perform operations
employees = [emp1, emp2, emp3]

for emp in employees:
    emp.show_info()
    yearly = emp.calculate_yearly_salary()
    print(f"Yearly Salary: ₹{yearly}")
    bonus = emp.apply_bonus()
    print(f"Bonus Applied ({int(bonus / (emp.salary - bonus) * 100)}%): ₹{bonus:.0f}")
    print("-" * 40)
    
    
# Output:
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: ₹75000
# Yearly Salary: ₹900000
# Bonus Applied (10%): ₹7500
# ----------------------------------------
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: ₹68000
# Yearly Salary: ₹816000
# Bonus Applied (8%): ₹5440
# ----------------------------------------
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: ₹80000
# Yearly Salary: ₹960000
# Bonus Applied (12%): ₹9600
# ----------------------------------------

    