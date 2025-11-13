# Employee Management Mini
# System
# Objective:
# Learn how to define a class, create multiple objects, and interact with them — just
# like how HR systems track employees in a company.

# Step 1: Create a class Employee with:
# Attribute Description
# emp_id Unique employee number
# name Full name of employee
# department e.g. IT, HR, Finance, Marketing
# salary Monthly salary

class Employee:
    def __init__(self,emp_id,name,dept,salary):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary

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

    def show_info(self):
        print(f"Employee ID:{self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee Department:{self.dept}")
        print(f"Employee Salary:{self.salary}")
    
    
    def apply_bonus(self):
        match self.dept:
            case "IT":
                self.salary+=self.salary*(.10)
                print(f"Bonus Applied 10%:{self.salary}")
            case "HR":
                self.salary+=self.salary*(.08)
                print(f"Bonus Applied 08%:{self.salary}")
            case "Finance":
                self.salary+=self.salary*(.12)
                print(f"Bonus Applied 12%:{self.salary}")
            case _:
                self.salary+=self.salary*(.05)
                print(f"Bonus Applied 05%:{self.salary}")

    def yearly_salary(self):
        return self.salary*12


emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

emp1.show_info()
print(f"Employee yearly salary:{emp1.yearly_salary()}")
emp1.apply_bonus()
print("----------------------------------")
emp2.show_info()
print(f"Employee yearly salary:{emp2.yearly_salary()}")
emp2.apply_bonus()
print("----------------------------------")
emp3.show_info()
print(f"Employee yearly salary:{emp3.yearly_salary()}")
emp3.apply_bonus()

# Sample output:
# Employee ID:101
# Employee Name:Arun Kumar
# Employee Department:IT
# Employee Salary:75000
# Employee yearly salary:900000
# Bonus Applied 10%:82500.0
# ----------------------------------
# Employee ID:102
# Employee Name:Riya Sharma
# Employee Department:HR
# Employee Salary:68000
# Employee yearly salary:816000
# Bonus Applied 08%:73440.0
# ----------------------------------
# Employee ID:103
# Employee Name:John Doe
# Employee Department:Finance
# Employee Salary:80000
# Employee yearly salary:960000
# Bonus Applied 12%:89600.0



