# # Task1:Human Resource Management System(HRMS)
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
    
    def __init__(self,emp_id,emp_name,base_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.base_salary=base_salary
    def show_details(self):
        print(f"Id: {self.emp_id}, name: {self.emp_name}, salary: {self.base_salary}")

class Developers(Employees):
    def __init__(self,emp_id,emp_name,base_salary,programming_languages):
        Employees.__init__(self,emp_id,emp_name,base_salary)
        self.programming_languages=programming_languages

    def show_skills(self):
        print(f"emp id:{self.emp_id},emp name: {self.emp_name}, emp sal: {self.base_salary}: skills: {', '.join(self.programming_languages)}")

class Manager(Employees):
    def __init__(self,emp_id,emp_name,base_salary,team_size , department):
        Employees.__init__(self,emp_id,emp_name,base_salary)
        self.team_size=team_size
        self.department=department
    def show_team_info(self):
        print(f"Manager emp_id: {self.emp_id}, emp name: {self.emp_name},emp sal: {self.base_salary}, emp team size: {self.team_size}, department: {self.department}")
# inherites the Developers and managers this is hybrid inheritence
class DeveloperManager(Developers,Manager):
    def __init__(self, emp_id, emp_name, base_salary,team_size,department, programming_languages):
        Developers.__init__(self,emp_id, emp_name, base_salary, programming_languages)
        Manager.__init__(self,emp_id, emp_name, base_salary,team_size,department)
    def get_details(self):
        print(f" Depeloper and Manager Id : {self.emp_id}, name: {self.emp_name}, base_salary : {self.base_salary},team size : {self.team_size}, department : {self.department}, programming_language : {self.programming_languages}")

emp=Employees(100,"Niru",30000)
emp.show_details()
emp1=Developers(101,"sai",45000,["java","Python"])
emp1.show_skills()
emp2=Manager(102,'naveen',78000,19,'IT')
emp2.show_team_info()
emp3=DeveloperManager(103,"praveen",100000,100,"IT",['java','python','ml'])
emp3.get_details()

    


# Id: 100, name: Niru, salary: 30000
# emp id:101,emp name: sai, emp sal: 45000: skills: java, Python
# Manager emp_id: 102, emp name: naveen,emp sal: 78000, emp team size: 19, department: IT
#  Depeloper and Manager Id : 103, name: praveen, base_salary : 100000,team size : 100, department : IT, programming_language : ['java', 'python', 'ml']

