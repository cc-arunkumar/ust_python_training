# Enterprise Tech Systems –
# Inheritance Design Challenge
# Objective:
# Design Python classes that model real-world enterprise systems using 
# inheritance appropriately.
# Each problem describes a business scenario — you must identify the right
# inheritance type and implement it cleanly.

# Task 1 — Human Resource Management System
# (HRMS)
# Domain: Corporate HR / Payroll
# Business Requirement:


# UST’s HR system needs to manage different types of employees.
# 1. All employees have:
# emp_id , name , base_salary
# Method: get_details() to display employee info
class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary

    def get_details(self):
        print(f"Employee Id:{self.emp_id}")
        print(f"Employee name:{self.name}")
        print(f"Employee salary:{self.base_salary}")

# 2. Developers have:
# programming_languages (list)
# Method: show_skills()
class Developers(Employee):
    def __init__(self,emp_id,name,base_salary,languages):
        Employee.__init__(self,emp_id,name,base_salary)
        self.programming_languages=languages

    def show_skills(self):
        print(f"Skills:{self.programming_languages}")

# 3. Managers have:
# team_size , department
# Method: show_team_info()
class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,team_size,department):
        Employee.__init__(self,emp_id,name,base_salary)
        self.team_size=team_size
        self.department=department

    def show_team_info(self):
        print(f"Manager Id:{self.emp_id}")
        print(f"Manager name:{self.name}")
        print(f"Manager salary:{self.base_salary}")
        print(f"Team size:{self.team_size}")
        print(f"Department:{self.department}")

# 4. Some managers are also developers (they code in emergencies).
# Task: Model this system so that “Manager who codes” can reuse both
# developer and manager features without rewriting logic.
# Enterprise Tech Systems – Inheritance Design Challenge 
class Dev_Man(Developers,Manager):
    def __init__(self,emp_id,name,base_salary,team_size,department,languages):

        Manager.__init__(self,emp_id,name,base_salary,team_size,department)
        Developers.__init__(self,emp_id,name,base_salary,languages)
      

    def show_all(self):
        self.get_details()
        self.show_skills()
        self.show_team_info()   

emp1=Employee(101,"Shahit",50000)
emp1.get_details()

print("-------------------------------------------------------------------------")

dev= Developers(101,"Amit",400000,["java","python"])
dev.get_details()
dev.show_skills()

print("-------------------------------------------------------------------------")

manager=Manager(101,"Arun",100000,30,"Cybersecurity")
manager.show_team_info()

print("-------------------------------------------------------------------------")

dev_man=Dev_Man(101,"Amit",500000,20,"Full stack",["java","python","c"])
dev_man.show_all()

# Sample output:
# Employee Id:101
# Employee name:Shahit
# Employee salary:50000
# -------------------------------------------------------------------------
# Employee Id:101
# Employee name:Amit
# Employee salary:400000
# Skills:['java', 'python']
# -------------------------------------------------------------------------
# Manager Id:101
# Manager name:Arun
# Manager salary:100000
# Team size:30
# Department:Cybersecurity
# -------------------------------------------------------------------------
# Employee Id:101
# Employee name:Amit
# Employee salary:500000
# Skills:['java', 'python', 'c']
# Manager Id:101
# Manager name:Amit
# Manager salary:500000
# Team size:20
# Department:Full stack
