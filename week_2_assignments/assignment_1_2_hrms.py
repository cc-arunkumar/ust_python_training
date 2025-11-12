# cretaing the base class
class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    def get_details(self):
        print(f"{self.emp_id}|{self.name}|{self.base_salary}")
# creating child classs that inherits from employee
class Developer(Employee):
    def __init__(self,emp_id,name,base_salary,programming_languages):
        Employee.__init__(self,emp_id,name,base_salary)
        self.programming_languages=programming_languages
    # programming_languages=["Python","C++"]
    def show_skills(self):
        print("skills:",self.programming_languages)
        
class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,team_size,department):
        Employee.__init__(self,emp_id,name,base_salary)
        self.team_size=team_size
        self.department=department
    def show_team_info(self):
        print(f"{self.team_size},{self.department}")
    
class DevManager(Developer,Manager):
    def __init__(self,emp_id,name,base_salary,programming_languages,team_size,department):
        Developer.__init__(self,emp_id,name,base_salary,programming_languages)
        Manager.__init__(self,emp_id,name,base_salary,team_size,department)
        
# checking if inheritence works

dev=Developer("E101","Arumukesh",120000.00,["Python"])
manager1=Manager("E103","Aashish",150000.00,8,"IT")
devman=DevManager("E109","Ajay",300000.00,["python"],9,"HR")
manager1.get_details()
dev.get_details()
devman.show_skills()


    
# E103|Aashish|150000.0
# E101|Arumukesh|120000.0
# skills: ['python']