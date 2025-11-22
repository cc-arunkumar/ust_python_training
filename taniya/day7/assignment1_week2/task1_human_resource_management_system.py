#  Task 1 — Human Resource Management System 
# (HRMS)
#  Domain: Corporate HR / Payroll
#  Business Requirement:
#  USTʼs HR system needs to manage different types of employees.
#   All employees have:
#  emp_id , 
# name , 
# base_salary
#  Method: 
# get_details() to display employee info
#   Developers have:
#  programming_languages (list)
#  Method: 
# show_skills()
#   Managers have:
#  team_size , 
# department
#  Method: 
# show_team_info()
#   Some managers are also developers (they code in emergencies)


class Employee:
     def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
        
     def get_details(self):
         print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.base_salary}")
 
        
class Developers(Employee):
        def __init__(self, emp_id, name, base_salary,programming_languages:list[str]):
             Employee.__init__(self,emp_id, name, base_salary) 
             self.programming_languages = programming_languages
        
        def show_skills(self):
               print(f"{self.name}'s Programming Skills: {(self.programming_languages)}")

                
class Managers(Employee):
        def __init__(self, emp_id, name, base_salary,team_size:int,department:str):
              Employee.__init__(self,emp_id, name, base_salary)
              self.team_size=team_size
              self.department=department
              
        def show_team_info(self):
              print(f"{self.name} manages {self.team_size} people in {self.department} department.")
              
class TechManager(Developers,Managers):
        def __init__(self, emp_id, name, base_salary, programming_languages:list[str],team_size,department):
              Developers.__init__(self,emp_id, name, base_salary, programming_languages)
              Managers.__init__(self,emp_id, name, base_salary, team_size,department)
              
              
              
tm1=TechManager(105,'Tanu',2934875.25,['Java',"Python",'C','C++','.Net','React',"Angular","SQL + NoSQL"],25,"HR")
tm2=TechManager(101,"Taniya",50000,["Java","python"],20,"IT")
tm3=TechManager(102,"Amit",60000,["Java"],15,"IT")             
tm4=TechManager(103,"Riya",40000,[],10,"HR")             
emp1=Employee(104,"Sonia",70000)

emp1.get_details()
# emp2.get_details()
# dev2.show_skills()

# mgr1.get_details()
# mgr1.show_team_info()
tm1.get_details()
tm1.show_skills()
tm1.show_team_info()
print("-------------------------------")
tm2.get_details()
tm2.show_skills()
tm2.show_team_info()
print("-------------------------------")
tm3.get_details()
tm3.show_skills()
tm3.show_team_info()
print("-------------------------------")
tm4.get_details()
tm4.show_skills()
tm4.show_team_info()


