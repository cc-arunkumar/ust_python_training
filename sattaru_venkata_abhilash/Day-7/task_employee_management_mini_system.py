# Employee Management Mini System
# Objective:
# Learn how to define a class, create multiple objects, and interact with them — just like how HR systems track employees in a company.
# Scenario:
# UST wants to build a very simple internal HR module in Python to store employee
# data temporarily and calculate key details.

# Define a class to represent an employee
class Employee:
    # Initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    # Display employee details
    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: ₹{self.salary}")

    # Calculate and return yearly salary
    def calculate_yearly_salary(self):
        yearly = self.salary * 12
        print(f"Yearly Salary: ₹{yearly}")
        return yearly

    # Apply bonus based on department
    def apply_bonus(self):
        if self.department == "IT":
            bonus = self.salary * 0.10
        elif self.department == "HR":
            bonus = self.salary * 0.08
        elif self.department == "Finance":
            bonus = self.salary * 0.12
        else:
            bonus = self.salary * 0.05
        
        new_salary = self.salary + bonus
        print(f"Bonus Applied ({int((bonus/self.salary)*100)}%): ₹{new_salary}")
        print("---------------------------------------")


# Create three employee objects
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Display details, yearly salary, and apply bonus for each employee
emp1.show_info()
emp1.calculate_yearly_salary()
emp1.apply_bonus()

emp2.show_info()
emp2.calculate_yearly_salary()
emp2.apply_bonus()

emp3.show_info()
emp3.calculate_yearly_salary()
emp3.apply_bonus()


# Sample Output:
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: ₹75000
# Yearly Salary: ₹900000
# Bonus Applied (10%): ₹82500.0
# ---------------------------------------
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: ₹68000
# Yearly Salary: ₹816000
# Bonus Applied (8%): ₹73440.0
# ---------------------------------------
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: ₹80000
# Yearly Salary: ₹960000
# Bonus Applied (12%): ₹89600.0
# ---------------------------------------
