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
# Task: Model this system so that “Manager who codes” can reuse both
# developer and manager features without rewriting logic.
# Enterprise Tech Systems – Inheritance Design Challenge 1

class Employee:
    # All employees have id,name,base_salary
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    # to display employee info
    def get_details(self):
        print(f"id:{self.emp_id},Name:{self.name},salary={self.base_salary}")
# developer class
class Developers(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
        self.programming_languges=programming_languages
    def show_skills(self):
        print(f"{self.name}'s programming skills:{','.join(self.programming_languges)},")
# Manager class
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        print(f"{self.name} manages {self.team_size} people in {self.department} department.")
class DevelopManagaer(Manager, Developers):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developers.__init__(self, emp_id, name, base_salary, programming_languages)

# Example usage
data = DevelopManagaer(101, "Priya", 95000, 10, "Tech", ["Python", "Java"])
data.get_details()
data.show_team_info()
data.show_skills()

# # output:
# id:101,Name:Priya,salary=95000
# Priya manages 10 people in Tech department.
# Priya's programming skills:Python,Java,
