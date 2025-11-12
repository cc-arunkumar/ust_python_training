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


class Employees:
    def __init__(self,emp_id,name,base_salary):
        self.emp_id=emp_id
        self.name=name
        self.base_salary=base_salary

    # Method to display employee details

    def get_details(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee salary: {self.base_salary}")

    # Subclass representing a Developer, inherits from Employees

class Developer(Employees):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        Employees.__init__(self,emp_id,name,base_salary)
        self.programming_languages=programming_languages

    
    # Method to show developer's programming skills
    def show_skills(self):
        print(f"{self.name} programming skills: {self.programming_languages}")


# Subclass representing a Manager, inherits from Employees

class Manager(Employees):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employees.__init__(self,emp_id,name,base_salary)
        self.team_size=team_size
        self.department=department
    def show_team_info(self):
        print(f"{self.name} is the manager of {self.department} with size of {self.team_size}")

class ManagerDeveloper(Manager, Developer):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)

# Creating a Developer object
dev = Developer(101,"Rahul",30000,["Python","SQL","Java"])
dev.get_details()
dev.show_skills()
print()

mgr=Manager(102,"charan",40000,5,"HR")
mgr.show_team_info()
print()

md=ManagerDeveloper(103,"Jignesh",65000,5,"Development",["Python","Java"])

md.get_details()
md.show_skills
md.show_team_info()
print()


# Sample Output
# Employee ID : 101
# Employee Name: Rahul
# Employee salary: 30000
# Rahul programming skills: ['Python', 'SQL', 'Java']

# charan is the manager of HR with size of 5

# Employee ID : 103
# Employee Name: Jignesh
# Employee salary: 65000
# Jignesh is the manager of Development with size of 5
