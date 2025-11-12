# task_1_employee_management_mini_system


# Step 1: Create a class Employee 

class Employee:
    def __init__(self,emp_id,name,dept,salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary
# Step 2: Add Methods
    def show_info(self):
        print(f"Employee ID:{self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee Dept:{self.dept}")
        print(f"Employee Salary:{self.salary}")

    def calculate_yearly_salary(self):
        self.salary = self.salary *12
        print(f"Yearly Salary:{self.salary}")

    def apply_bonus(self):
        if self.dept == "IT":
            bonus_percentage = 0.10

        elif self.dept == "HR":
            bonus_percentage = 0.8

        elif self.dept == "Finance":
            bonus_percentage = 0.12
        
        else:
            bonus_percentage = 0.5

        bonus_amount = self.salary * bonus_percentage   
        self.salary += bonus_amount
        print(f"Bonus Applied({bonus_percentage}):{self.salary}")

# 3.creating an object of the Employee class
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# 4: Perform Operations
employees = [emp1, emp2, emp3]

# Step 4: Display details, yearly salary, and apply bonus for each employee
for emp in employees:
    emp.show_info()
    emp.calculate_yearly_salary()
    emp.apply_bonus()

# -----------------------------------------------------------------------------------------

# Sample Output

# Employee ID:101
# Employee Name:Arun Kumar
# Employee Dept:IT
# Employee Salary:75000
# Yearly Salary:900000
# Bonus Applied(0.1):990000.0
# Employee ID:102
# Employee Name:Riya Sharma
# Employee Dept:HR
# Employee Salary:68000
# Yearly Salary:816000
# Bonus Applied(0.8):1468800.0
# Employee ID:103
# Employee Name:John Doe
# Employee Dept:Finance
# Employee Salary:80000
# Yearly Salary:960000
# Bonus Applied(0.12):1075200.0




