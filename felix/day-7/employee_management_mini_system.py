# UST wants to build a very simple internal HR module in Python to store employee
# data temporarily and calculate key details.
# Each Employee should have:
# emp_id
# name
# department
# salary
# and should be able to:
# Display personal details
# Calculate yearly salary
# Apply a bonus based on department


# Source Code


# Step 1 Creating class Employee
class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        
    # Step 2 Creating methods show_info, calculate_yearly_salary, add_bonous
    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Monthly Salary: {self.salary}")
        
    def calculate_yearly_salary(self):
        print(f"Yearly Salary: {self.salary*12}")
        
    def add_bonous(self):
        match self.department:
            case "IT":
                self.salary += self.salary*10/100
                print(f"Bonous Applied (10%): ${int(self.salary)}")
            case "HR":
                self.salary += self.salary*8/100
                print(f"Bonous Applied (8%): ${int(self.salary)}")
            case "Finance":
                self.salary += self.salary*12/100
                print(f"Bonous Applied (12%): ${int(self.salary)}")
            case _:
                self.salary += self.salary*5/100
                print(f"Bonous Applied (5%): ${int(self.salary)}")
                
                
                
            
# step 3 creating objects for Employee class

emp1 = Employee(101,"Arun Kumar","IT",75000)
emp2 = Employee(102,"Riya Sharma","HR",68000)
emp3 = Employee(103,"John Doe","Finance",80000)

# Step 4 Output

emp1.show_info()
emp1.calculate_yearly_salary()
emp1.add_bonous()
print("---------------------------------")
emp2.show_info()
emp2.calculate_yearly_salary()
emp2.add_bonous()
print("---------------------------------")
emp3.show_info()
emp3.calculate_yearly_salary()
emp3.add_bonous()

# # output

# Employee ID: 101
# Employee Name: Arun Kumar
# Employee Department: IT
# Monthly Salary: 75000
# Yearly Salary: 900000
# Bonous Applied (10%): $82500
# ---------------------------------
# Employee ID: 102
# Employee Name: Riya Sharma
# Employee Department: HR
# Monthly Salary: 68000
# Yearly Salary: 816000
# Bonous Applied (8%): $73440
# ---------------------------------
# Employee ID: 103
# Employee Name: John Doe
# Employee Department: Finance
# Monthly Salary: 80000
# Yearly Salary: 960000
# Bonous Applied (12%): $89600