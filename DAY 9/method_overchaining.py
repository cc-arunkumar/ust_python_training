# Base class to store basic employee information
class Employee:
    def __init__(self, id, name, dept):
        self.id = id          # Employee ID
        self.name = name      # Employee Name
        self.dept = dept      # Department



# Developer class inherits from Employee
# Adds platform information
class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id, name, dept)   # Initialize parent class attributes
        self.platform = platform           # Platform (e.g., iOS, Android)
    
    # Display developer information
    def show_details(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Department :", self.dept)
        print("Platform :", self.platform)



# Frontend developer class inheriting from Developer
class Frontend(Developer):
    def __init__(self, id, name, dept, platform, skill):
        super().__init__(id, name, dept, platform)   # Call Developer constructor
        self.skill = skill                           # Frontend-specific skill
    
    # Display all details including skill
    def show_details(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Department :", self.dept)
        print("Platform :", self.platform)
        print("Skill set :", self.skill)



# Backend developer class inheriting from Developer
class Backend(Developer):
    def __init__(self, id, name, dept, platform, skill):
        super().__init__(id, name, dept, platform)   # Inherit developer attributes
        self.skill = skill                           # Backend-specific skill
    
    # Display full backend developer details
    def show_details(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Department :", self.dept)
        print("Platform :", self.platform)
        print("Skill set :", self.skill)



# Creating objects and displaying details

d1 = Developer(1, "Gowtham", "R/D", "IOs")
d1.show_details()

f1 = Frontend(2, "Mani", "IT", "IOS", "React")
f1.show_details()

b1 = Backend(3, "Dk", "Devops", "Android", "Angular")
b1.show_details()


"""
SAMPLE OUTPUT

ID : 1
Name : Gowtham
Department : R/D
Platform : IOs
ID : 2
Name : Mani
Department : IT
Platform : IOS
Skill set : React
ID : 3
Name : Dk
Department : Devops
Platform : Android
Skill set : Angular
"""