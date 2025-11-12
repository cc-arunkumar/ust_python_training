class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
    
    #function to show details
    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Employee Salary: {self.salary}")
    
    #function to print yearly salary    
    def calculate_yearly_salary(self):
        print(f"Yearly Salary of {self.name} is {self.salary*12}")
    
    #function to apply bonus based on department
    def apply_bonus(self):
        if self.department == 'IT':
            self.salary += self.salary*0.10
            print(f"Bonus Applied (10%):{self.salary}")
        elif self.department == 'HR':
            self.salary += self.salary*0.08
            print(f"Bonus Applied (8%):{self.salary}")
        elif self.department == 'Finance':
            self.salary += self.salary*0.12
            print(f"Bonus Applied (12%):{self.salary}")
        else:
            self.salary += self.salary*0.05
            print(f"Bonus Applied (5%):{self.salary}")

#Object creation    
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

#Calling the functions
emp1.show_info()
emp1.calculate_yearly_salary()
emp1.apply_bonus()
print("=================================")

emp2.show_info()
emp2.calculate_yearly_salary()
emp2.apply_bonus()
print("=================================")

emp3.show_info()
emp3.calculate_yearly_salary()
emp3.apply_bonus()
print("=================================")


#Sample Output
# Employee ID: 101
# Employee Name: Arun Kumar
# Employee Department: IT
# Employee Salary: 75000
# Yearly Salary of Arun Kumar is 900000 
# Bonus Applied (10%):82500.0
# =================================     
# Employee ID: 102
# Employee Name: Riya Sharma
# Employee Department: HR
# Employee Salary: 68000
# Yearly Salary of Riya Sharma is 816000
# Bonus Applied (8%):73440.0
# =================================     
# Employee ID: 103
# Employee Name: John Doe
# Employee Department: Finance
# Employee Salary: 80000
# Yearly Salary of John Doe is 960000
# Bonus Applied (12%):89600.0
# =================================
