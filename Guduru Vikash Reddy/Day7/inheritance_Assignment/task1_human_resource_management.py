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
# 2. Developers have:
# programming_languages (list)
# Method: show_skills()
# 3. Managers have:
# team_size , department
# Method: show_team_info()
# 4. Some managers are also developers (they code in emergencies).
# ⚙️ Task: Model this system so that “Manager who codes” can reuse both
# developer and manager features without rewriting logic.
# Enterprise Tech Systems – Inheritance Design Challenge 1
# �� Hint for participants: think about multiple inheritance vs multilevel, and which
# combination fits best.

# Define the base class for all employees
class Employees:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    
    def get_details(self):
        print(f"Employee id:",self.emp_id)
        print(f"Employee name:",self.name)
        print(f"Employee base salary:",self.base_salary)

# Extend Employees to include developer-specific attributes
class Developers(Employees):
    def __init__(self,emp_id,name,base_salary,programming_lists):
        Employees.__init__(self,emp_id,name,base_salary)
        self.programming_lists=programming_lists
    
    def show_skills(self):
        print(f"Name:",self.name,"programming skills:",self.programming_lists)

# Extend Employees to include manager-specific attributes
class Managers(Employees):
    def __init__(self, emp_id, name, base_salary,team_size,department):
        Employees.__init__(self,emp_id,name,base_salary)
        self.team_size=team_size
        self.department=department
    
    def show_team_info(self):
        print(f"Team size",self.team_size,"Departments in",self.department)

# Combine Developer and Manager roles using multiple inheritance
class DeveloperManager(Developers,Managers):
    def __init__(self, emp_id, name, base_salary, programming_lists,team_size,department):
        Developers.__init__(self,emp_id,name,base_salary,programming_lists)
        Managers.__init__(self,emp_id,name,base_salary,team_size,department)


emp1=Developers(1,"ashok",50000,["python","java"],)


emp2=Managers(2,"manoj",70000,10,"it")


emp1.get_details()
emp1.show_skills()


emp2.get_details()
emp2.show_team_info()

# sample output
# Employee id: 1
# Employee name: ashok       
# Employee base salary: 50000
# Name: ashok programming skills: ['python', 'java']
# Employee id: 2
# Employee name: manoj
# Employee base salary: 70000
# Team size 10 Departments in it

