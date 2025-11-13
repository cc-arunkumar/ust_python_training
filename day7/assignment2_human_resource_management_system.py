

# Multiple inheritance

# UST’s HR system needs to manage different types of employees.

# All employees have:
# emp_id , name , base_salary
# Method: get_details() to display employee info
class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    def get_details(self):
        print(f"ID: {self.emp_id},Name:{self.name},Salary:{self.base_salary}")
        
#  Developers have:
# programming_languages (list)
# Method: show_skills()
    
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary,programming_languages):
        Employee.__init__(self,emp_id,name,base_salary)
        self.programming_languages=programming_languages
    
    def show_skills(self):
        print(f"{self.name} knows: {self.programming_languages}")

# Managers have:
# team_size , department
# Method: show_team_info()

class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,team_size,department):
        Employee.__init__(self,emp_id,name,base_salary)
        self.team_size=team_size
        self.department=department
    
    def show_team_info(self):
        print(f"{self.name} manages {self.team_size} people in {self.department} department.")
        
# Some managers are also developers (they code in emergencies).
        
class ManagerCodes(Manager,Developer):
    def __init__(self,emp_id,name,base_salary,team_size,department,programming_languages):
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)
        
        
# developer      
dev = Developer(101, "varsha", 60000, ["Python", "Java"])
dev.get_details()
dev.show_skills()
print("******************************************")

# manager
mgr = Manager(102, "Tharun", 80000, 10, "IT")
mgr.get_details()
mgr.show_team_info()
print("******************************************")

# Manager who codes
mgr_dev = ManagerCodes(103,"Bhargavi",90000,5,"R&D",["C++", "Go"])
mgr_dev.get_details()
mgr_dev.show_team_info()
mgr_dev.show_skills()      



# output

# ID: 101,Name:varsha,Salary:60000
# varsha knows: ['Python', 'Java']

# ******************************************  
# ID: 102,Name:Tharun,Salary:80000
# Tharun manages 10 people in IT department. 
 
# ******************************************  
# ID: 103,Name:Bhargavi,Salary:90000
# Bhargavi manages 5 people in R&D department.
# Bhargavi knows: ['C++', 'Go']
