# Base class for all employees
class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
    
    # Method to display employee details
    def get_details(self):
        print(f"Employee emp_id: {self.emp_id}")
        print(f"Employee name: {self.name}")
        print(f"Base salary: {self.base_salary}")
        

# Developer class inherits from Employee
class Developer(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, programming_languages: list):
        # Call Employee constructor
        Employee.__init__(self, emp_id, name, base_salary)
        self.programming_languages = programming_languages
        
    # Method to show developer skills
    def show_skills(self):
        if self.programming_languages:
            print(f"{self.name}'s skills: {', '.join(self.programming_languages)}")
        else:
            print(f"{self.name} has no skills")
            

# Manager class inherits from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        # Call Employee constructor
        Employee.__init__(self, emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department
        
    # Method to show manager's team info
    def show_team_info(self):
        print(f"Department: {self.department}, Team Size: {self.team_size}")
        

# DevManager inherits from both Developer and Manager (multiple inheritance)
class DevManager(Developer, Manager):
    def __init__(self, emp_id, name, base_salary, programming_languages, team_size, department):
        # Initialize both Developer and Manager parts
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        

# ------------------- Testing the classes -------------------
print("------------------------------------------")
e1 = Employee(101, "Rohit", 70000) 
e1.get_details()

print("------------------------------------------")
d1 = Developer(102, "Prithvi", 65000, ["SQL", "Python"])
d1.get_details()
d1.show_skills()

print("------------------------------------------")
m1 = Manager(103, "Sohan", 77800, 5, "HR")
m1.get_details()
m1.show_team_info()

print("------------------------------------------")
dm1 = DevManager(104, "Harsh", 90000, ["Java", "Python", "C++"], 6, "IT")
dm1.get_details()
dm1.show_skills()
dm1.show_team_info()
print("------------------------------------------")


# ------------------------------------------
# Employee emp_id:101
# Employee name:Rohit
# Base salary:70000
# ------------------------------------------
# Employee emp_id:102
# Employee name:Prithvi
# Base salary:65000
# Prithvi's skills: SQL, Python
# ------------------------------------------
# Employee emp_id:103
# Employee name:Sohan
# Base salary:77800
# Department: HR, Team Size: 5
# ------------------------------------------
# Employee emp_id:103
# Employee name:Harsh
# Base salary:90000
# Harsh's skills: Java, Python, C++
# Department: IT, Team Size: 6
# ------------------------------------------