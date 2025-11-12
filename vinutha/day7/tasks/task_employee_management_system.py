
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: Rs.{self.salary}")

    def calculate_yearly_salary(self):
        return self.salary * 12

    def bonus(self):
        bonus_percentage = {
            "IT": 0.10,
            "HR": 0.08,
            "Finance": 0.12
        }.get(self.department, 0.05)
        bonus_amount = self.salary * (1 + bonus_percentage)
        return bonus_amount, bonus_percentage


# Create Employee objects
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Perform Operations
employees = [emp1, emp2, emp3]

for emp in employees:
    emp.show_info()
    yearly_salary = emp.calculate_yearly_salary()
    bonus_salary, bonus_percent = emp.bonus()
    print(f"Yearly Salary: Rs.{yearly_salary}")
    print(f"Bonus Applied ({int(bonus_percent * 100)}%): Rs.{int(bonus_salary)}")
    print("*******************************************")

# #output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day7/task1_employee_management_system.py
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.82500
# ---------------------------------------
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: Rs.68000
# ---------------------------------------
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.89600
# ---------------------------------------
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day7/task1_employee_management_system.py
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.82500
# *******************************************
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: Rs.68000
# *******************************************
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.89600
# *******************************************
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day7/task1_employee_management_system.py
# Employee ID: 101
# Name: Arun Kumar
# Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.82500
# *******************************************
# Employee ID: 102
# Name: Riya Sharma
# Department: HR
# Monthly Salary: Rs.68000
# Yearly Salary: Rs.816000
# Bonus Applied (8%): Rs.73440
# *******************************************
# Employee ID: 103
# Name: John Doe
# Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.89600
# *******************************************
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day7>