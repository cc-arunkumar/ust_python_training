"""
UST wants to build a very simple internal HR module in Python to store employee data temporarily and calculate key details.

"""

class Employee:
    
    def __init__(self,emp_id,name,dep,salary):
        self.emp_id=emp_id
        self.name=name
        self.dep=dep
        self.salary=salary
    
    def self_info(self):
        print(f"Employee ID :{self.emp_id}")
        print(f"Name :{self.name}")
        print(f"Department :{self.dep}")
        print(f"Monthly Salary : ₹{self.salary}")

    def calculate_yearly(self):
        yearly_salary=self.salary*12
        print(f"Yearly salary of {self.name} is ₹ {yearly_salary}")

    def apply_bonus(self):
        if self.dep=="IT":
            self.salary+=(self.salary*0.10)
            print(f"Bonus applied (10%):₹ {self.salary}")
        elif self.dep=="HR":
            self.salary+=(self.salary*0.08)
            print(f"Bonus applied (8%):₹ {self.salary}")
        elif self.dep=="Finance":
            self.salary+=(self.salary*0.12)
            print(f"Bonus applied (12%):₹ {self.salary}")
        elif self.dep=="Others":
            self.salary+=(self.salary*0.05)
            print(f"Bonus applied (5%):₹ {self.salary}")
        else: print("Enter a valid Department")
        
# Creating Object for 3 Employees
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# employee complete data
print("---Employee 1---")
emp1.self_info()
emp1.calculate_yearly()
emp1.apply_bonus()

# employee 2
print("---Employee 2---")
emp2.self_info()
emp2.calculate_yearly()
emp2.apply_bonus()

#employee 3
print("---Employee 3---")
emp3.self_info()
emp3.calculate_yearly()
emp3.apply_bonus()


"""
SAMPLE OUTPUT

---Employee 1---
Employee ID :101
Name :Arun Kumar
Department :IT
Monthly Salary : ₹75000
Yearly salary of Arun Kumar is ₹ 900000
Bonus applied (10%):₹ 82500.0
---Employee 2---
Employee ID :102
Name :Riya Sharma
Department :HR
Monthly Salary : ₹68000
Yearly salary of Riya Sharma is ₹ 816000
Bonus applied (8%):₹ 73440.0
---Employee 3---
Employee ID :103
Name :John Doe
Department :Finance
Monthly Salary : ₹80000
Yearly salary of John Doe is ₹ 960000
Bonus applied (12%):₹ 89600.0
"""