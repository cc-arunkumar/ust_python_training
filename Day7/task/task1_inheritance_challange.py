# UST wants to build a very simple internal HR module in Python to store employee data temporarily and calculate key details.

# Base class
class All_employees:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

# Subclass 1 — Developers
class Developers(All_employees):
    def __init__(self, emp_id, name, salary, programming_languages):
        All_employees.__init__(self, emp_id, name, salary)
        self.programming_languages = programming_languages

    def show_skills(self):
        print(f"Programming Languages:{self.programming_languages}")
        

# Subclass 2 — Managers
class Managers(All_employees):
    def __init__(self, emp_id, name, salary, team_size, department):
        All_employees.__init__(self, emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def show_team_info(self):
        print(f"Team size: {self.team_size}, Department: {self.department}")

#DeveloperManager Class
class DeveloperManager(Developers, Managers):
    def __init__(self, emp_id, name, salary, programming_languages, team_size, department):
        Developers.__init__(self, emp_id, name, salary, programming_languages)
        Managers.__init__(self, emp_id, name, salary, team_size, department)

    def show_all_info(self):
        self.get_details()
        self.show_skills()
        self.show_team_info()


#Testing
dev = Developers(101, "Madhan", 30000, ["Java", "C++"])
print("\n--- Developer Info ---")
dev.get_details()
dev.show_skills()

mgr = Managers(102, "Kumar", 80000, 10, "IT")
print("\n--- Manager Info ---")
mgr.get_details()
mgr.show_team_info()

mgr_dev = DeveloperManager(103, "Madhan", 95000, 8, "AI Dept", ["Python", "C++"])
print("\n--- Developer and Manager ---")
mgr_dev.show_all_info()

# sample output:
# --- Developer Info ---
# Employee ID: 101
# Employee Name: Madhan
# Employee Salary: 30000
# Programming Languages:['Java', 'C++']

# --- Manager Info ---
# Employee ID: 102
# Employee Name: Kumar
# Employee Salary: 80000
# Team size: 10, Department: IT

# --- Developer and Manager ---
# Employee ID: 103
# Employee Name: Madhan
# Employee Salary: 95000
# Programming Languages:8
# Team size: AI Dept, Department: ['Python', 'C++']
