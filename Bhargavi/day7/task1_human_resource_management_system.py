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
#  Hint for participants: think about multiple inheritance vs multilevel, and which
# combination fits best


# Base class
class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.base_salary}")

# Developer class
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        Employee.__init__(self, emp_id, name, base_salary)
        self.programming_languages = programming_languages

    def show_skills(self):
        print(f"{self.name} knows: {', '.join(self.programming_languages)}")

# Manager class
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employee.__init__(self, emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department
    
    #method to get department data
    def show_team_info(self):
        print(f"{self.name} manages a team of {self.team_size} in {self.department} department")

# Management class using multiple inheritance
class Management(Developer, Manager):
    def __init__(self, emp_id, name, base_salary, programming_languages, team_size, department):
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)

# Createing an instance
m = Management(emp_id=201,name="Bhargavi S", base_salary=120000,programming_languages=["C++", "Go"],team_size=5,
    department="Cybersecurity"
)

# Access all methods
m.get_details()
m.show_skills()
m.show_team_info()

#output

# ID: 201, Name: Bhargavi S, Salary: 120000
# Bhargavi S knows: C++, Go
# Bhargavi S manages a team of 5 in Cybersecurity department