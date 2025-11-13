# Task 1 — Human Resource Management System(HRMS)
#  All employees have:
# emp_id , name , base_salary
# Method: get_details() to display employee info

class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        print(f"Employee ID: {self.emp_id} | Name: {self.name} | Base Salary: ₹{self.base_salary}")

#  Developers have:
# programming_languages (list)
# Method: show_skills()

class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        Employee.__init__(self,emp_id, name, base_salary)
        self.programming_languages = programming_languages

    def show_skills(self):
        print(f"{self.name}'s skills are: {', '.join(self.programming_languages)}")
#  Managers have:
# team_size , department
# Method: show_team_info()

class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        print(f"Department: {self.department} | Team Size: {self.team_size}")


class DevManagers(Manager, Developer):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)



emp1 = Employee(101, "Rahul", 75000)
emp2 = Employee(102, "Rishi", 68000)
emp1.get_details()
emp2.get_details()
print("------------------")


dev1 = Developer(103, "Taniya", 85000, ["Python", "C", "Java"])
dev1.get_details()
dev1.show_skills()
print("------------------")

mang1 = Manager(104, "John Doe", 80000, 5, "Finance")
mang1.get_details()
mang1.show_team_info()
print("------------------")

dev_mang = DevManagers(105, "Soni", 95000, 8, "IT", ["Go", "Rust", "JavaScript"])
dev_mang.get_details()
dev_mang.show_team_info()
dev_mang.show_skills()
print("------------------")

# sample output
# Employee ID: 101 | Name: Rahul | Base Salary: ₹75000
# Employee ID: 102 | Name: Rishi | Base Salary: ₹68000
# ------------------
# Employee ID: 103 | Name: Taniya | Base Salary: ₹85000
# Taniya's skills are: Python, C, Java
# ------------------
# Employee ID: 104 | Name: John Doe | Base Salary: ₹80000
# Department: Finance | Team Size: 5
# ------------------
# Employee ID: 105 | Name: Soni | Base Salary: ₹95000
# Department: IT | Team Size: 8
# Soni's skills are: Go, Rust, JavaScript
# ------------------