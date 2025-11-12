# Task 1 — Human Resource Management System
# (HRMS)
# Domain: Corporate HR / Payroll

# Base class
class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
    
    def show_info(self):
        print(f"Employee ID :{self.emp_id}")
        print(f"Name:{self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly salary: ₹{self.salary}")
        print(f"Yearly salary: ₹{self.calculate_yearly_salary()}")
        

    def calculate_yearly_salary(self):
        return self.salary*12

    def apply_bonus(self,department,bonus):
        if(department=="IT"):
            self.salary += (bonus*self.salary)/100
            print(f"Bonus Applied(bonus)%: ₹{self.salary}")
        elif(department=="HR"):
            self.salary += (bonus*self.salary)/100
            print(f"Bonus Applied(bonus)%: ₹{self.salary}")
        elif(department=="Finance"):
            self.salary += (bonus*self.salary)/100
            print(f"Bonus Applied(bonus)%: ₹{self.salary}")
        elif(department=="Others"):
            self.salary += (bonus*self.salary)/100
            print(f"Bonus Applied(bonus)%: ₹{self.salary}")
#Testing
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

emp1.show_info()
emp1.apply_bonus("IT",10)
print("---------------------------------------")

emp2.show_info()
emp1.apply_bonus("HR",8)
print("---------------------------------------")

emp3.show_info()
emp1.apply_bonus("Finance",12)
print("---------------------------------------")

# sample output:

# Employee ID :101
# Name:Arun Kumar
# Department: IT
# Monthly salary: ₹75000
# Yearly salary: ₹900000
# Bonus Applied(bonus)%: ₹82500.0
# ---------------------------------------
# Employee ID :102
# Name:Riya Sharma
# Department: HR
# Monthly salary: ₹68000
# Yearly salary: ₹816000
# Bonus Applied(bonus)%: ₹89100.0
# ---------------------------------------       
# Employee ID :103
# Name:John Doe
# Department: Finance
# Monthly salary: ₹80000
# Yearly salary: ₹960000
# Bonus Applied(bonus)%: ₹99792.0
# ---------------------------------------  

