#Task 1 — Human Resource Management System(HRMS)
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

#Main Class
class Employee:

    def __init__(self,emp_id,name,base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
    
    def get_details(self):
        print(f"Employee Id : {self.emp_id}")
        print(f"Name : {self.name}")
        print(f"Salary : {self.base_salary}")

#Sub-class
class Developer(Employee):

    def __init__(self, emp_id, name, base_salary,program_lang:list[str]):
        Employee.__init__(self,emp_id, name, base_salary)
        self.program_lang = program_lang

    def show_skills(self):
        self.get_details()
        print(f"Skills : {self.program_lang}")

#Sub-class
class Manager(Employee):

    def __init__(self, emp_id, name, base_salary,team_size,dep):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.dep = dep
    
    def show_team_info(self):
        self.get_details()
        print(f"Team size : {self.team_size} Department : {self.dep}")

#Sub-class
class DevManager(Developer,Manager):
    
    def __init__(self, emp_id, name, base_salary, program_lang,team_size,dep):
        Developer.__init__(self,emp_id,name,base_salary, program_lang)
        Manager.__init__(self,emp_id,name,base_salary,team_size,dep)
    
    def show(self):
        self.get_details()
        print(f"Skills : {self.program_lang}")
        print(f"Team size : {self.team_size} Department : {self.dep}")
    
#Creating the object
e1 = Developer(101,"Arjun",12000,["Python,Java"])
e2 = Manager(102,"Rahul",13000,5,"IT")
e3 = DevManager(103,"Ravi",12000,["Python"],5,"IT")
e3.show()

#Output
# Employee Id : 103
# Name : Ravi
# Salary : 12000
# Skills : ['Python']
# Team size : 5 Department : IT

    