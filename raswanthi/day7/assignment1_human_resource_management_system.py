#Assignment 1: Human Resource Management System using Inheritance

class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        print(f"Employee ID: {self.emp_id} | Name: {self.name} | Base Salary: ₹{self.base_salary}")

#class Developer inheriting properties from Employee
class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        Employee.__init__(self,emp_id, name, base_salary)
        self.programming_languages = programming_languages

    def show_skills(self):
        print(f"{self.name}'s skills are: {', '.join(self.programming_languages)}")

#class MAnager inheriting from Employee class
class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        Employee.__init__(self,emp_id, name, base_salary)
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        print(f"Department: {self.department} | Team Size: {self.team_size}")

#class DevManagers includes behaviors of both Manager and Developer
class DevManagers(Manager, Developer):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
        Manager.__init__(self, emp_id, name, base_salary, team_size, department)
        Developer.__init__(self, emp_id, name, base_salary, programming_languages)


# Creating object instances
emp1 = Employee(101, "Arun Kumar", 75000)
emp2 = Employee(102, "Riya Sharma", 68000)
emp1.get_details()
emp2.get_details()
print("------------------")


dev1 = Developer(103, "Tara", 85000, ["Java", "Python", "C"])
dev1.get_details()
dev1.show_skills()
print("------------------")

mang1 = Manager(104, "John Doe", 80000, 5, "Finance")
mang1.get_details()
mang1.show_team_info()
print("------------------")

dev_mang = DevManagers(105, "Sneha", 95000, 8, "IT", ["Go", "Rust", "JavaScript"])
dev_mang.get_details()
dev_mang.show_team_info()
dev_mang.show_skills()
print("------------------")

#output:
'''
Employee ID: 101 | Name: Arun Kumar | Base Salary: ₹75000
Employee ID: 102 | Name: Riya Sharma | Base Salary: ₹68000
------------------
Employee ID: 103 | Name: Tara | Base Salary: ₹85000
Employee ID: 101 | Name: Arun Kumar | Base Salary: ₹75000
Employee ID: 102 | Name: Riya Sharma | Base Salary: ₹68000
------------------
Employee ID: 103 | Name: Tara | Base Salary: ₹85000
Employee ID: 102 | Name: Riya Sharma | Base Salary: ₹68000
------------------
Employee ID: 103 | Name: Tara | Base Salary: ₹85000
Tara's skills are: Java, Python, C
------------------
Employee ID: 104 | Name: John Doe | Base Salary: ₹80000
Department: Finance | Team Size: 5
------------------
Employee ID: 105 | Name: Sneha | Base Salary: ₹95000
Department: IT | Team Size: 8
Sneha's skills are: Go, Rust, JavaScript
------------------
'''