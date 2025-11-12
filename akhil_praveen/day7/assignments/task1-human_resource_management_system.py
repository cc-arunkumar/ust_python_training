# Human Resource Management System

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

#Main Parent class
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary = salary
    def get_details(self):
        print(f"Employee id = {self.id}")
        print(f"Employee name = {self.name}")
        print(f"Employee base salary = {self.salary}")
        
# Child class
class Developers(Employee):
    def __init__(self, id, name, salary,skills:list[str]):
        Employee.__init__(self, id, name, salary)
        self.skills=skills
    def show_skills(self):
        print("Skills: ")
        for i in self.skills:
            print(i)

# child class
class Manager(Employee):
    def __init__(self, id, name, salary,size:int,dept:str):
        Employee.__init__(self, id, name, salary)
        self.team_size=size
        self.dept=dept
    def show_team_info(self):
        print(f"Team size = {self.team_size}")
        print(f"Department name = {self.dept}")

# child class by multiple inheritance
class DevManager(Developers,Manager):
    def __init__(self, id, name, salary, skills,size,dept):
        
        Developers.__init__(self,id, name, salary, skills)
        Manager.__init__(self,id, name, salary, size, dept)


# Creating objects for each and getting info
emp1 = Employee(101, 'Akhil', 23425.25)
emp1.get_details()

print("***************************")

dev1 = Developers(102,"Arjun", 927452.25,["Java","Python"])
dev1.get_details()
dev1.show_skills()

print("***************************")

mgr1 = Manager(103,'Felix', 9234875.25,5,'IT')
mgr1.get_details()
mgr1.show_team_info()

print("***************************")

dev_mgr1 = DevManager(104,'Ashutosh',928375.25,['.Net','React','Python'],8,'HR')
dev_mgr1.get_details()
dev_mgr1.show_skills()
dev_mgr1.show_team_info()

# Output
# Employee id = 101
# Employee name = Akhil
# Employee base salary = 23425.25
# ***************************
# Employee id = 102
# Employee name = Arjun
# Employee base salary = 927452.25
# Skills:
# Java
# Python
# ***************************
# Employee id = 103
# Employee name = Felix
# Employee base salary = 9234875.25
# Team size = 5
# Department name = IT
# ***************************
# Employee id = 104
# Employee name = Ashutosh
# Employee base salary = 928375.25
# Skills:
# .Net
# React
# Python
# Team size = 8
# Department name = HR

