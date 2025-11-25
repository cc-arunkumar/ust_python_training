# Design Python classes that model real-world enterprise systems using 
# inheritance appropriately.
# Each problem describes a business scenario — you must identify the right
# inheritance type and implement it cleanly.



# Task 1 — Human Resource Management System
# (HRMS)
# Domain: Corporate HR / Payroll
# Business Requirement:
# UST’s HR system needs to manage different types of employees.
from typing import List

# Base class representing a generic Employee
class Employee:
    def __init__(self, emp_id, name, base_salary):
        # Initialize employee ID, name, and base salary
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        
    def get_details(self):
        # Print employee details
        print(self.emp_id, self.name, self.base_salary)


# Class representing Developers (specialized employees with programming skills)
class Developers:
    def __init__(self, programming_language: List[str]):
        # Initialize list of programming languages known by the developer
        self.programming_language = programming_language or []
        
    def show_skills(self):
        # Print developer skills as a comma-separated string
        print("Skills:", ", ".join(self.programming_language))


# Class representing Managers (specialized employees managing teams)
class Managers:
    def __init__(self, team_size, department):
        # Initialize manager's team size and department
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        # Print manager's team information
        print(self.team_size, " ", self.department)


# Class representing Developer-Managers (employees who are both developers and managers)
# Demonstrates multiple inheritance: inherits from both Developers and Managers
class DevManagers(Developers, Managers):
    def __init__(self, team_size, department, programming_language):
        # Initialize Developers part of DevManagers
        Developers.__init__(self, programming_language)
        # Initialize Managers part of DevManagers
        Managers.__init__(self, team_size, department)


# Create an instance of DevManagers with team size, department, and programming skills
emp1 = DevManagers(5, "IT", {"Java", "Python"})

# Print heading text
print("Showing information")
# Call method from Managers class to show team info
emp1.show_team_info()

# Print heading text
print("skills")
# Call method from Developers class to show programming skills
emp1.show_skills()


# ==============sample- output===================
# Showing information 
# 5   IT
# skills
# Skills: Java, Python