# Enterprise Tech Systems –
# Inheritance Design Challenge
# Objective:
# Design Python classes that model real-world enterprise systems using 
# inheritance appropriately.
# Each problem describes a business scenario — you must identify the right
# inheritance type and implement it cleanly.



# Task 1 — Human Resource Management System
# (HRMS)
# Domain: Corporate HR / Payrol

# Create Employee Class
# All employees have:
# emp_id , name , base_salary
# Method: get_details() to display employee info

class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.base_salary}")


# Developer Class
# Developers have:
# programming_languages (list)
# Method: show_skills()

class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        Employee.__init__(self,emp_id, name, base_salary)
        self.programming_languages = programming_languages

    def show_skills(self):
        print("--------------------------")
        print(f"Developer Name: {self.name}")
        print(f"Programming Languages: {', '.join(self.programming_languages)}")


# Manager Class
# Managers have:
# team_size , department
# Method: show_team_info()

class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        print("--------------------------")
        print(f"Manager Name: {self.name} ") 
        print(f"Manager Id:{self.emp_id}") 
        print(f"Manager Salary: {self.base_salary}") 
        print(f"Team Size: {self.team_size}") 
        print(f"Department: {self.department}")


# Create DeveloperManager Class 
# Some managers are also developers (they code in emergencies).

class DeveloperManager(Manager, Developer):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
        
        # Employee.__init__(self, emp_id, name, base_salary)
        # self.team_size = team_size
        # self.department = department
        # self.programming_languages = programming_languages
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)

    def get_details(self):
        print("--------------------------")
        print(f"Manager Who can develope")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: {self.base_salary}")
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")
        print(f"Programming Languages: {', '.join(self.programming_languages)}")


emp1 = Employee(101, "Arun Kumar", 75000)
emp2 = Developer(102, "Riya Sharma", 68000, ["Java", "Python"])
emp3 = Manager(103, "Niranjan", 80000, 5, "Finance")
emp4 = DeveloperManager(104, "Sai", 95000, 8, "IT", ["Python", "C++"])


emp1.get_details()
emp2.get_details()
emp2.show_skills()
emp3.get_details()
emp3.show_team_info()
emp4.get_details()

# Sample Output
# Employee ID: 101
# Employee Name: Arun Kumar
# Employee Salary: 75000
# Employee ID: 102
# Employee Name: Riya Sharma
# Employee Salary: 68000
# --------------------------
# Developer Name: Riya Sharma
# Programming Languages: Java, Python
# Employee ID: 103
# Employee Name: Niranjan
# Employee Salary: 80000
# --------------------------
# Manager Name: Niranjan
# Manager Id:103
# Manager Salary: 80000
# Team Size: 5
# Department: Finance
# --------------------------
# Manager Who can develope
# Employee ID: 104
# Employee Name: Sai
# Base Salary: 95000
# Department: IT
# Team Size: 8
# Programming Languages: Python, C++