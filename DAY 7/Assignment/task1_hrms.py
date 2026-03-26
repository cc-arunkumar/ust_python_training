"""
Model this system so that “Manager who codes” can reuse both developer and manager features without rewriting logic.
"""
# Base class representing a general employee
class Employees:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id          # Employee ID
        self.name = name              # Employee name
        self.base_salary = base_salary  # Base salary of the employee
    
    # Method to display employee details
    def get_details(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name : {self.name}")
        print(f"Base salary : {self.base_salary}")


# Developer class inherits from Employees
class Developers(Employees):
    def __init__(self, emp_id, name, base_salary, programming_lang):
        # Initialize base employee attributes
        Employees.__init__(self, emp_id, name, base_salary)
        self.programming_lang = programming_lang  # List of programming languages
    
    # Method to show the developer skills
    def show_skills(self):
        print(f"{self.name} knows {self.programming_lang}")


# Manager class inherits from Employees
class Managers(Employees):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        # Initialize base employee attributes
        Employees.__init__(self, emp_id, name, base_salary)
        self.team_size = team_size      # Number of team members
        self.department = department    # Department name
    
    # Method to display manager-specific info
    def show_team_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Department : {self.department}")
        print(f"Team Size: {self.team_size}")


# DeveloperManager class inherits both Developers and Managers
# Allows reuse of both developer and manager features
class DeveloperManager(Developers, Managers):
    def __init__(self, emp_id, name, base_salary, programming_lang, team_size, department):
        # Initialize developer part
        Developers.__init__(self, emp_id, name, base_salary, programming_lang)
        # Initialize manager part
        Managers.__init__(self, emp_id, name, base_salary, team_size, department)
    
    # Method to display combined info
    def dev_manager_info(self):
        print(f"Developer Manager Name : {self.name}")
        print(f"{self.name} knows {self.programming_lang}")
        print(f"Department : {self.department}")
        print(f"Team Size: {self.team_size}")


# Example usage

# Developers info
print("---Developer---")
dev1 = Developers("D1", "Naveen", 20000, ["C++", "java"])
dev1.get_details()      # Display basic employee info
dev1.show_skills()      # Display developer skills

# Managers info
print("---Manager---")
man1 = Managers("M1", "Varum", 50000, 8, "IT")
man1.get_details()      # Display basic employee info
man1.show_team_info()   # Display manager-specific info

# Developer Managers info
print("---DEveloper manager---")
devman1 = DeveloperManager("DM1", "Karthick", 75000, ["C++", "JavaScript"], 10, "R/D")
devman1.get_details()       # Display basic employee info
devman1.dev_manager_info()  # Display combined developer-manager info


"""
SAMPLE OUTPUT

---Developer---
Employee ID :Naveen
Name :Naveen
Base salary :20000
Naveen knows ['C++', 'java']
---Manager---
Employee ID :Varum
Name :Varum
Base salary :50000
Manager Name: Varum
Department :IT
Team Size: 8
---DEveloper manager---
Employee ID :Karthick
Name :Karthick
Base salary :75000
Developer Manager Name :Karthick
Karthick knows ['C++', 'JavaScript']
Department :R/D
Team Size: 10
"""