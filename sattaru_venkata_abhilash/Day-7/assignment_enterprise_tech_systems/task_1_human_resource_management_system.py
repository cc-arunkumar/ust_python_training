# Task 1 — Human Resource Management System (HRMS)
# Domain: Corporate HR / Payroll
# Objective:
# Demonstrate multiple inheritance where a Manager can also be a Developer.

# Base class representing a general employee
class Employee:
    def __init__(self, emp_id, name, base_salary):
        # Initialize employee details
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    # Display basic employee details
    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: ₹{self.base_salary}")


# Derived class for Developers (inherits from Employee)
class Developers(Employee):
    def __init__(self, emp_id, name, base_salary, programming_languages):
        # Call Employee constructor to initialize common attributes
        Employee.__init__(self, emp_id, name, base_salary)
        # Store developer-specific information
        self.programming_languages = programming_languages

    # Display developer's skills
    def show_skills(self):
        print(f"\nDeveloper: {self.name}")
        print("Programming Languages:", ", ".join(self.programming_languages))


# Derived class for Managers (inherits from Employee)
class Managers(Employee):
    def __init__(self, emp_id, name, base_salary, team_size, department):
        # Call Employee constructor to initialize base attributes
        Employee.__init__(self, emp_id, name, base_salary)
        # Store manager-specific attributes
        self.team_size = team_size
        self.department = department

    # Display manager's department and team information
    def show_team_info(self):
        print(f"\nManager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")


# Multiple inheritance class — a Manager who can also code
class DeveloperManager(Managers, Developers):
    def __init__(self, emp_id, name, base_salary, team_size, department, programming_languages):
        # Initialize both parent classes (Manager and Developer)
        Managers.__init__(self, emp_id, name, base_salary, team_size, department)
        Developers.__init__(self, emp_id, name, base_salary, programming_languages)

    # Display complete details for a Manager who codes
    def get_details(self):
        print("\n--- Manager Who Codes ---")
        Employee.get_details(self)
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")
        print("Programming Languages:", ", ".join(self.programming_languages))


# -------------------------------------------------------------
# Object Creation and Demonstration
# -------------------------------------------------------------
if __name__ == "__main__":
    # Create objects for each type of employee
    emp1 = Employee(101, "Vikas", 75000)
    emp2 = Developers(102, "Niranjan", 68000, ["Python", "JavaScript"])
    emp3 = Managers(103, "Sai", 80000, 10, "Finance")
    emp4 = DeveloperManager(104, "Abhi", 95000, 8, "IT", ["Python", "C++", "SQL"])
    emp5 = DeveloperManager(105, "Shakeel", 92000, 7, "HR", ["Java", "HTML", "CSS"])
    emp6 = DeveloperManager(106, "SRK", 97000, 12, "R&D", ["Python", "Go", "Docker"])

    # Display details for a regular employee
    print("\n--- Employee ---")
    emp1.get_details()

    # Display details for a developer
    print("\n--- Developer ---")
    emp2.get_details()
    emp2.show_skills()

    # Display details for a manager
    print("\n--- Manager ---")
    emp3.get_details()
    emp3.show_team_info()

    # Display details for managers who are also developers
    emp4.get_details()
    emp5.get_details()
    emp6.get_details()


# Sample Output:
# --- Employee ---
# Employee ID: 101
# Employee Name: Vikas
# Base Salary: ₹75000

# --- Developer ---
# Employee ID: 102
# Employee Name: Niranjan
# Base Salary: ₹68000

# Developer: Niranjan
# Programming Languages: Python, JavaScript

# --- Manager ---
# Employee ID: 103
# Employee Name: Sai
# Base Salary: ₹80000

# Manager: Sai
# Department: Finance
# Team Size: 10

# --- Manager Who Codes ---
# Employee ID: 104
# Employee Name: Abhi
# Base Salary: ₹95000
# Department: IT
# Team Size: 8
# Programming Languages: Python, C++, SQL

# --- Manager Who Codes ---
# Employee ID: 105
# Employee Name: Shakeel
# Base Salary: ₹92000
# Department: HR
# Team Size: 7
# Programming Languages: Java, HTML, CSS

# --- Manager Who Codes ---
# Employee ID: 106
# Employee Name: SRK
# Base Salary: ₹97000
# Department: R&D
# Team Size: 12
# Programming Languages: Python, Go, Docker
