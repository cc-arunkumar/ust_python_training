# Enterprise Tech Systems –
# Inheritance Design Challenge
# Objective:
# Design Python classes that model real-world enterprise systems using 
# inheritance appropriately.
# Each problem describes a business scenario — you must identify the right
# inheritance type and implement it cleanly.
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
# 4. Some managers are also developers (they code in emergencies

#Base parent class Employee
class Employee:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary
    
    def get_details(self):
        print("Employee ID: ",self.emp_id)
        print("Name: ",self.name)
        print("Base Salary: ",self.base_salary)

#child class of employee
class Developers(Employee):
    def __init__(self,emp_id,name,base_salary,programming_languages:list[str]):
        #for creating the employee
        Employee.__init__(self,emp_id,name,base_salary)
        self.programming_languages=programming_languages
    
    def show_skills(self):
        for skill in self.programming_languages:
            if skill!=None:
                print(skill,end=",")
        print()
#child class of employee
class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,team_size,department):
        #for creating the employee
        Employee.__init__(self,emp_id,name,base_salary)
        self.team_size=team_size
        self.department=department
    
    def show_team_info(self):
        print("size of team: ",self.team_size,"Department",self.department)

#child class of both manager and developer
class DeveloperManager(Manager,Developers):
    def __init__(self,emp_id,name,base_salary,team_size,department,programming_languages:list[str]):
        #creating the manager
        Manager.__init__(self,emp_id,name,base_salary,team_size,department)
        #creating the developer
        Developers.__init__(self,emp_id,name,base_salary,programming_languages)
    
        
emp1=Manager(101,"shyam",5000,6,"HR")
emp1.get_details()
emp1.show_team_info()
print("-------------------------")

emp2=Developers(102,"ram",5000,["Python","Java","C++"])
emp2.get_details()
emp2.show_skills()   
print("-------------------------")

emp3=DeveloperManager(103,"venkat",8000,10,"IT",["Python","Java"])
emp3.get_details()
emp3.show_team_info()
emp3.show_skills()
print("-------------------------")

#Sample output
# Employee ID:  101
# Name:  shyam
# Base Salary:  5000
# size of team:  6 Department HR 
# -------------------------      
# Employee ID:  102
# Name:  ram
# Base Salary:  5000
# Python,Java,C++,
# -------------------------      
# Employee ID:  103
# Name:  venkat
# Base Salary:  8000
# size of team:  10 Department IT
# Python,Java,
# -------------------------