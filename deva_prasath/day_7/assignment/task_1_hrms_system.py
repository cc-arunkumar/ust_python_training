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

# Employee class to store basic employee details
class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid  # Employee ID
        self.name = name    # Employee Name
        self.salary = salary  # Employee Salary
        
    def get_details(self):
        # Print employee details
        print(f"Employee ID is {self.empid}")
        print(f"Employee Name is {self.name}")
        print(f"Employee Salary is {self.salary}")

# Developer class inheriting from Employee, adds programming skills
class Developer(Employee):
    def __init__(self, empid, name, salary, programming_lan):
        Employee.__init__(self, empid, name, salary)  # Inherit from Employee
        self.programming_lan = programming_lan  # Developer's programming skills
    
    def show_skills(self):
        # Show each programming language skill
        for i in self.programming_lan:
            print(f"The skills are {i}")

# Manager class inheriting from Employee, adds team-related attributes
class Manager(Employee):
    def __init__(self, empid, name, salary, team_size, department):
        Employee.__init__(self, empid, name, salary)  # Inherit from Employee
        self.team_size = team_size  # Manager's team size
        self.department = department  # Manager's department
        
    def show_team_info(self):
        # Show manager and team information
        print(f"Manager ID is {self.empid}")
        print(f"Manager Name is {self.name}")
        print(f"Manager Salary is {self.salary}")
        print(f"Team Size is {self.team_size}")
        print(f"Department is {self.department}")

# ManagerDeveloper class inherits from both Manager and Developer
class ManagerDeveloper(Manager, Developer):
    def __init__(self, empid, name, salary, team_size, department, programming_lan):
        Developer.__init__(self, empid, name, salary, programming_lan)  # Initialize Developer
        Manager.__init__(self, empid, name, salary, team_size, department)  # Initialize Manager

# Object creation and method calls
dev1 = Developer('001', 'Deva', 100000, ["Python", "Java", "C", "C++"])  # Create Developer object
dev1.get_details()  # Print Developer details
dev1.show_skills()  # Show Developer skills
print("-----------------------------")
man = Manager('100', 'Arun', 20000, 10, "HR")  # Create Manager object
man.show_team_info()  # Show Manager's team info
print("------------------------------")
md = ManagerDeveloper('111', 'Asutosh', 300000, 20, "Board of Directors", ["Javascript", "Node", "SQL", "Ruby"])  # Create ManagerDeveloper object
md.get_details()  # Print ManagerDeveloper details
md.show_skills()  # Show ManagerDeveloper's skills


#Sample output

# Employee ID is 001
# Employee Name is Deva
# Employee Salary is 100000
# The skills are Python
# The skills are Java
# The skills are C
# The skills are C++
# -----------------------------
# Manager ID is 100
# Manager Name is Arun
# Manager Salary is 20000
# Team Size is 10
# Department is HR
# ------------------------------
# Employee ID is 111
# Employee Name is Asutosh
# Employee Salary is 300000
# The skills are Javascript
# The skills are Node
# The skills are SQL
# The skills are Ruby
