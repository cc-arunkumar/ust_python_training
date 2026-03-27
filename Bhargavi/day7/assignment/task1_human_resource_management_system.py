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


# Task 1 — Human Resource Management System (HRMS)
# Demonstrates inheritance and multiple inheritance in Python

# Base class for all employees
class Employee:
    def __init__(self, emp_id, name, base_salary):
        # Common attributes for all employees
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
    
    def get_details(self):
        # Method to display employee details
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.base_salary}")


# Developer class inherits from Employee
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        # Call Employee constructor to initialize common attributes
        Employee.__init__(self, emp_id, name, base_salary)
        self.programming_languages = programming_languages
    
    # Method to display developer's programming skills
    def show_skills(self):
        print(f"{self.name} knows: {', '.join(self.programming_languages)}")


# Manager class inherits from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employee.__init__(self, emp_id, name, base_salary)
        # Manager-specific attributes
        self.team_size = team_size
        self.department = department
    
    # Method to display manager's team details
    def show_team_info(self):
        print(f"{self.name} manages a team of {self.team_size} in {self.department} department")


# Management class using multiple inheritance
# Combines both Developer and Manager features
class Management(Developer, Manager):
    def __init__(self, emp_id, name, base_salary, programming_languages, team_size, department):
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)
        # Initialize Manager part
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)


# Create an instance of Management (Manager who codes)
m = Management(emp_id=201,name="Bhargavi S",base_salary=120000,programming_languages=["C++", "Go"],team_size=5,department="Cybersecurity")

# Access all methods from Employee, Developer, and Manager
m.get_details()      # From Employee
m.show_skills()      # From Developer
m.show_team_info()   # From Manager


#output
# ID: 201, Name: Bhargavi S, Salary: 120000
# Bhargavi S knows: C++, Go
# Bhargavi S manages a team of 5 in Cybersecurity department