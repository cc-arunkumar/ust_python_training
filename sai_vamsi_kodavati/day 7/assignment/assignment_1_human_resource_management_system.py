# assignment_1_Task 1 — Human Resource Management System

# All employees have:
# emp_id , name , base_salary
# Method: get_details() to display employee info


class Employees:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        print(f"Employee ID:{self.emp_id}")
        print(f"Employee Name:{self.name}")
        print(f"Employee Base Salary:{self.base_salary}")

#  Developers have:
# programming_languages (list)
# Method: show_skills()
        
class Developers(Employees):
    def __init__(self,emp_id,name,base_salary,programming_languages):
        Employees.__init__(self,emp_id,name,base_salary)
        self.programming_languages = programming_languages

    def show_skills(self):
        print(f"Programming Languages:{",".join(self.programming_languages)}")

#  Managers have:
# team_size , department
# Method: show_team_info()

class Manager(Employees):
    def __init__(self,emp_id,name,base_salary,team_size,department):
        Employees.__init__(self,emp_id,name,base_salary)
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        print(f"Team Size:{self.team_size}")
        print(f"Department:{self.department}")

# Some managers are also developers (they code in emergencies).


class ManagerDeveloper(Developers,Manager):
    def __init__(self,emp_id,name,base_salary,team_size,department,programming_languages):
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developers.__init__(self, emp_id, name, base_salary, programming_languages)


emp1 = Employees(101,"Sai Vamsi",10000)
print("\n---Employees---")
emp1.get_details()       


dev1 = Developers(102,"Venky",20000,["Java","Python"])
print("\n ----Developers----")
dev1.get_details()
dev1.show_skills()


mgr = Manager(103,"Sarthak",30000,10,"IT")
print("\n ----Manager----")
mgr.get_details()
mgr.show_team_info()


mgrdev = ManagerDeveloper(104,"Tharun",40000,14,"HR",["Java","Python"])
print("\n ----ManagerDeveloper----")
mgrdev.get_details()
mgrdev.show_skills()
mgrdev.show_team_info()

# ---------------------------------------------------------------------------------

# Sample Output

# ---Employees---
# Employee ID:101
# Employee Name:Sai Vamsi
# Employee Base Salary:10000

#  ----Developers----
# Employee ID:102
# Employee Name:Venky
# Employee Base Salary:20000
# Programming Languages:Java,Python

#  ----Manager----
# Employee ID:103
# Employee Name:Sarthak
# Employee Base Salary:30000
# Team Size:10
# Department:IT

#  ----ManagerDeveloper----
# Employee ID:104
# Employee Name:Tharun
# Employee Base Salary:40000
# Programming Languages:Java,Python
# Team Size:14
# Department:HR