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

# Define Class Employee
class Employee:
    # Creating constructor
    def __init__(self,emp_id,name,base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
    
    # Printing details of employee
    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Base Salary: {self.base_salary}")
        
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary,programming_language):
        Employee.__init__(self,emp_id, name, base_salary)
        self.programming_language = programming_language
        
    
    def show_skills(self):
        print(f"Skills of Employee {self.name} are:")
        for language in self.programming_language:
            print(language)
            
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary,team_size,department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department
        
    def show_team_info(self):
        print(f"Team Size: {self.team_size}")
        print(f"Department: {self.department}")
        
class DeveloperManager(Developer,Manager):
    def __init__(self, emp_id, name, base_salary, programming_language,team_size,department):
        Developer.__init__(self,emp_id, name, base_salary, programming_language)
        Manager.__init__(self,emp_id, name, base_salary, team_size,department)
    
# Creating Objects for all classes
emp1 = Employee(101,"Felix",50000)
emp2 = Employee(102,"Akhil",60000)
emp3 = Employee(103,"Arun",70000)
emp4 = Employee(104,"Arjun",80000)

emp5 = Developer(101,"Felix",50000,["Python","Java"])
emp5.show_skills()
print("--------------------------------")
emp6 = Manager(102,"Arun",80000,5,"IT")
emp6.show_team_info()   
print("--------------------------------")
emp7 = DeveloperManager(103,"Akhil",70000,["Python","Java"],6,"HR")
emp7.show_skills()
emp7.show_team_info()     