# Task 1 — Human Resource Management System (HRMS)

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


class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id = emp_id 
        self.name = name 
        self.base_salary = base_salary
        
    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Base Salary : {self.base_salary}")

class Developer(Employee):
    def __init__(self,emp_id, name, base_salary, programming_languages_list : list[str]):
        Employee.__init__(self,emp_id,name,base_salary)
        self.programming_list = programming_languages_list
        
    def show_skills(self):
        print(f"Skills of {self.name}: {self.programming_list}")
            
class Manager(Employee):
    def __init__(self,emp_id, name, base_salary,team_size,department):
        Employee.__init__(self,emp_id,name,base_salary)
        self.team_size = team_size 
        self.department = department
    
    def show_team_info(self):
        print(f"Manager {self.name} Team:")
        print(f"Team Size: {self.team_size}")
        print(f"Department: {self.department}")

class ManagerDeveloper(Manager,Developer):
    def __init__(self,emp_id,name,base_salary,team_size,department,programming_languages_list: list[str]):
        Developer.__init__(self,emp_id,name,base_salary,programming_languages_list)
        Manager.__init__(self,emp_id,name,base_salary,team_size,department)
    def show():
        print("Its DevManager")
    
dv1 = Developer(101,"Anjan",13000,["Python","C","Java",'yml'])
dv1.show_skills()
            
manager1 = Manager(102,"Ramesh",13344,10,'HR')
manager1.show_team_info()

print("DevManger Details:")
devmanager = ManagerDeveloper(103,"Arun",30000,11,"Finance",["Python","HTML","Java"])
devmanager.show_skills()
devmanager.get_details()

        
        
         
#Sample Output 
# Skills of Anjan: ['Python', 'C', 'Java', 'yml']
# Manager Ramesh Team:
# Team Size: 10
# Department: HR
# DevManger Details:
# Skills of Arun: ['Python', 'HTML', 'Java']
# Employee ID: 103
# Name: Arun
# Base Salary : 30000    