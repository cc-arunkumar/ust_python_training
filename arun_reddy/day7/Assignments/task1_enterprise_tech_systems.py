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
# ⚙️ Task: Model this system so that “Manager who codes” can reuse both
# developer and manager features without rewriting logic.



class Employees:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    
    
    def get_details(self):
        print("Employee Details...:")
        print(f"Employee id: {self.emp_id}")
        print(f"Employee name:{self.name}")
        print(f"Emploee base_salary:{self.base_salary}")
        
        
# Develoepers extends Employees 
class Developers(Employees):
    def __init__(self, emp_id, name, base_salary,programminglanguages):
        Employees.__init__(self,emp_id, name, base_salary)
        self.programminglanguages=programminglanguages
    def show_skills(self):
        print(f"The Skills of the{self.name} Employees are :")
        for skill in self.programminglanguages:
            print(f"{skill}")

# Mnagers extends Employees 
class Managers(Employees):
    def __init__(self,emp_id, name, base_salary,teamsize,department):
        Employees.__init__(self, emp_id, name, base_salary,)
        self.teamsize=teamsize
        self.department=department
    
    def show_team_info(self):
        print(f"Teamsize : {self.teamsize}")
        print(f"Department :{self.department}")
        
# Developermanager extends Developers,Managers
class Developermanager(Developers,Managers):
    def __init__(self,empid,name,base_salary,programminglanguages,teamsize,department):
        Developers.__init__(self,empid,name,base_salary,programminglanguages)
        Managers.__init__(self,empid,name,base_salary,teamsize,department)

    
# creating the object and calling the methods 
dev1=Developers(1022,"Arun",67000,["C","C++","python"])
dev1.show_skills()
    
dev1=Developers(1023,"Arjun",67000,["Java","C++","python"])
dev1.show_skills()


Mang=Managers(1023,"Arjun",67000,9,"Finanace")
Mang.show_team_info()
devman=Developermanager(1023,"Arjun",67000,["Java","C++","python"],9,"Finance")
devman.show_skills()
devman1=Developermanager(1024,"Aryan",80999,["Python","C","C++"],9,"HR")
devman1.show_skills()
    

# sample execution
# The Skills of theArun Employees are :
# C
# C++
# python
# The Skills of theArjun Employees are :
# Java
# C++
# python
# Teamsize : 9
# Department :Finanace
# The Skills of theArjun Employees are :
# Java
# C++
# python
# The Skills of theAryan Employees are :
# Python
# C
# C++