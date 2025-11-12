"""
Model this system so that “Manager who codes” can reuse both developer and manager features without rewriting logic.
"""
class Employees:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    
    def get_details(self):
        print(f"Employee ID :{self.name}")
        print(f"Name :{self.name}")
        print(f"Base salary :{self.base_salary}")

class Developers(Employees):
    def __init__(self, emp_id, name, base_salary,programming_lang):
        Employees.__init__(self,emp_id, name, base_salary)
        self.programming_lang=programming_lang

    def show_skills(self):
        print(f"{self.name} knows {self.programming_lang}")

class Managers(Employees):
    def __init__(self, emp_id, name, base_salary,team_size , department):
        Employees.__init__(self,emp_id, name, base_salary)
        self.team_size=team_size
        self.department=department
    
    def show_team_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Department :{self.department}")
        print(f"Team Size: {self.team_size}")

class DeveloperManager(Developers,Managers):
    def __init__(self, emp_id, name, base_salary, programming_lang,team_size,department):
        Developers.__init__(self,emp_id, name, base_salary, programming_lang)
        Managers.__init__(self,emp_id, name, base_salary,team_size , department)
    
    def dev_manager_info(self):
        print(f"Developer Manager Name :{self.name}")
        print(f"{self.name} knows {self.programming_lang}")
        print(f"Department :{self.department}")
        print(f"Team Size: {self.team_size}")


# For Employees
# emp1=Employees(1,"Gowtham",10000)
# emp1.get_details()

# Developers info
print("---Developer---")
dev1=Developers("D1","Naveen",20000,["C++","java"])
dev1.get_details()
dev1.show_skills()

#Managers
print("---Manager---")
man1=Managers("M1","Varum",50000,8,"IT")
man1.get_details()
man1.show_team_info()

# Developer Managers
print("---DEveloper manager---")
devman1=DeveloperManager("DM1","Karthick",75000,["C++","JavaScript"],10,"R/D")
devman1.get_details()
devman1.dev_manager_info()

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