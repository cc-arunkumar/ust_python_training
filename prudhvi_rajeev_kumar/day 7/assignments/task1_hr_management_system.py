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
# 4. Some managers are also developers (they code in emergencies).
# ⚙️ Task: Model this system so that “Manager who codes” can reuse both
# developer and manager features without rewriting logic.
# Enterprise Tech Systems – Inheritance Design Challenge 1
# �� Hint for participants: think about multiple inheritance vs multilevel, and which
# combination fits best


class Employee:
    #Adding the Required attributes of the Employee class.
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def getdetails(self):
        print(f"Employee Id: {self.emp_id}, Employee Name: {self.name}, Base Salary: {self.base_salary}")

#Creating a developer class and inheriting the properties of it.
class Developer(Employee):
    def __init__(self, programming_languages, emp_id, name, base_salary):
        self.programming_languages = programming_languages or []
        Employee.__init__(self, emp_id, name, base_salary)

    def show_skills(self):
        print("Programming Languages:", ', '.join(self.programming_languages))

#Creating a Managers Class and inheriting the properties of it.
class Managers(Employee):
    def __init__(self, team_size, department, emp_id, name, base_salary):
        self.team_size = team_size
        self.department = department
        Employee.__init__(self, emp_id, name, base_salary)

    def show_team_size(self):
        print(f"Team Size: {self.team_size}, Department: {self.department}")

#Inheriting another class ManagerWhoCodes from Employee class.
class ManagerWhoCodes(Employee):
    def __init__(self, programming_languages, team_size, department, emp_id, name, base_salary):
        self.programming_languages = programming_languages
        self.team_size = team_size
        self.department = department
        Employee.__init__(self, emp_id, name, base_salary)

    def show_skills(self):
        print("Programming Languages:", ', '.join(self.programming_languages))

    def show_team_size(self):
        print(f"Team Size: {self.team_size}, Department: {self.department}")

# Example usage
e1 = Employee(1001, 'Prudhvi Rajeev Kumar', 75000)
e1.getdetails()
print("******************************************************************************")
d1 = Developer(['Python', 'Java', 'C++', 'JavaScript', 'C#'], 1002, 'Alice', 80000)
d1.getdetails()
d1.show_skills()
print("******************************************************************************")
m1 = Managers(10, 'IT', 1003, 'Bob', 90000)
m1.getdetails()
m1.show_team_size()
print("*****************************************************************************")
mc1 = ManagerWhoCodes(['Python', 'JavaScript'], 5, 'Engineering', 1004, 'Charlie', 95000)
mc1.getdetails()
mc1.show_skills()
mc1.show_team_size()



#Console Output:
# Employee Id: 1001, Employee Name: Prudhvi Rajeev Kumar, Base Salary: 75000
# ***************************************************************************

# Employee Id: 1002, Employee Name: Alice, Base Salary: 80000
# Programming Languages: Python, Java, C++, JavaScript, C#
# ***************************************************************************

# Employee Id: 1003, Employee Name: Bob, Base Salary: 90000
# Team Size: 10, Department: IT
# ***************************************************************************

# Employee Id: 1004, Employee Name: Charlie, Base Salary: 95000
# Programming Languages: Python, JavaScript
# Team Size: 5, Department: Engineering
#****************************************************************************