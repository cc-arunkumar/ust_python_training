# Employee Management Mini System
stack = []
bonus = {"IT":0.1,
         "HR":0.08,
         "Finance":0.12
         }
class Employee:
    def __init__(self,id,name,dept,salary):
        if id not in stack:
            self.id = id
            self.name = name
            self.dept = dept
            self.salary = salary
            stack.append(self.id)
            
        else:
            print(f"{id} already exists! Object not created.\n")
    def show_info(self):
        print(f"Employee id: {self.id}\n")
        print(f"Employee name: {self.name}\n")
        print(f"Employee department: {self.dept}\n")
        print(f"Employee salary: {self.salary}\n")
    def calculate_yearly_salary(self):
        print(f"Yearly salary of {self.name} is {self.salary*12}\n")
        
    def bonus(self):
        if self.dept in bonus:
            self.salary+=(self.salary*bonus[self.dept])
        else:
            self.salary+=(self.salary*0.05)

        print(f"Salary of {self.name} who in department {self.dept} is increased to {self.salary} per month.\n")
 
# creating new objects for employees 
emp1 = Employee(101,"Akhil","IT",100000)

emp2 = Employee(102,"Arjun","HR",100000)

emp3 = Employee(101, "Arun Kumar", "Finance", 75000)

emp3 = Employee(103, "Arun Kumar", "Finance", 75000)

# display emp status
emp1.show_info()
emp2.show_info()
emp3.show_info()

# Yearly salary of each employee

emp1.calculate_yearly_salary()
emp2.calculate_yearly_salary()
emp3.calculate_yearly_salary()

# Bonus given to employee
emp1.bonus()
emp2.bonus()
emp3.bonus()

# Output

# 101 already exists! Object not created.

# Employee id: 101

# Employee name: Akhil

# Employee department: IT

# Employee salary: 100000

# Employee id: 102

# Employee name: Arjun

# Employee department: HR

# Employee salary: 100000

# Employee id: 103

# Employee name: Arun Kumar

# Employee department: Finance

# Employee salary: 75000

# Yearly salary of Akhil is 1200000

# Yearly salary of Arjun is 1200000

# Yearly salary of Arun Kumar is 900000

# Salary of Akhil who in department IT is increased to 110000.0 per month.

# Salary of Arjun who in department HR is increased to 108000.0 per month.

# Salary of Arun Kumar who in department Finance is increased to 84000.0 per month.