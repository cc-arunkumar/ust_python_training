# -------------------------------
# Task 1 — Human Resource Management System (HRMS)
# Domain: Corporate HR / Payroll
# Business Requirement:
# UST's HR system needs to manage different types of employees:
# 1. All employees have emp_id, name, base_salary and method get_details()
# 2. Developers have programming_languages and method show_skills()
# 3. Managers have team_size, department and method show_team_info()
# 4. Some managers are also developers (TechManager class)
# -------------------------------

# Base class for all employees
class Employee:
    def __init__(self, emp_id, name, base_salary):
        # Initialize employee attributes
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        # Display employee details
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.base_salary}")


# Developers class inherits from Employee
class Developers(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages: list[str]):
        # Call Employee constructor
        Employee.__init__(self, emp_id, name, base_salary)
        # Store developer's programming languages
        self.programming_languages = programming_languages

    def show_skills(self):
        # Display developer's programming skills
        print(f"{self.name}'s Programming Skills: {self.programming_languages}")


# Managers class inherits from Employee
class Managers(Employee):
    def __init__(self, emp_id, name, base_salary, team_size: int, department: str):
        # Call Employee constructor
        Employee.__init__(self, emp_id, name, base_salary)
        # Store manager-specific attributes
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        # Display manager's team information
        print(f"{self.name} manages {self.team_size} people in {self.department} department.")


# TechManager class inherits from both Developers and Managers
class TechManager(Developers, Managers):
    def __init__(self, emp_id, name, base_salary, programming_languages: list[str], team_size, department):
        # Initialize Developer part
        Developers.__init__(self, emp_id, name, base_salary, programming_languages)
        # Initialize Manager part
        Managers.__init__(self, emp_id, name, base_salary, team_size, department)


# -------------------------------
# Object Creation
# -------------------------------

# Create TechManager objects
tm1 = TechManager(105, 'Tanu', 2934875.25,
                  ['Java', "Python", 'C', 'C++', '.Net', 'React', "Angular", "SQL + NoSQL"],
                  25, "HR")

tm2 = TechManager(101, "Taniya", 50000, ["Java", "python"], 20, "IT")
tm3 = TechManager(102, "Amit", 60000, ["Java"], 15, "IT")
tm4 = TechManager(103, "Riya", 40000, [], 10, "HR")

# Create a simple Employee object
emp1 = Employee(104, "Sonia", 70000)

# -------------------------------
# Method Calls
# -------------------------------

# Display details of Employee
emp1.get_details()

# Display details of TechManager objects
tm1.get_details()
tm1.show_skills()
tm1.show_team_info()
print("-------------------------------")

tm2.get_details()
tm2.show_skills()
tm2.show_team_info()
print("-------------------------------")

tm3.get_details()
tm3.show_skills()
tm3.show_team_info()
print("-------------------------------")

tm4.get_details()
tm4.show_skills()
tm4.show_team_info()


# -------------------------------
# Program Output
# -------------------------------
# ID: 104, Name: Sonia, Salary: 70000
# ID: 105, Name: Tanu, Salary: 2934875.25
# Tanu's Programming Skills: ['Java', 'Python', 'C', 'C++', '.Net', 'React', 'Angular', 'SQL + NoSQL']
# Tanu manages 25 people in HR department.
# -------------------------------
# ID: 101, Name: Taniya, Salary: 50000
# Taniya's Programming Skills: ['Java', 'python']
# Taniya manages 20 people in IT department.
# -------------------------------
# ID: 102, Name: Amit, Salary: 60000
# Amit's Programming Skills: ['Java']
# Amit manages 15 people in IT department.
# -------------------------------
# ID: 103, Name: Riya, Salary: 40000
# Riya's Programming Skills: []
# Riya manages 10 people in HR department.