#Employee Management Mini System
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
bonus={
    "IT":10,
    "HR":8,
    "Finance":12
}
L=[]
class Employee:
    def __init__(self,emp_id,name,dep,salary):
        if emp_id not in L:
            self.emp_id=emp_id
            self.name=name
            self.dep=dep
            self.salary=salary
            L.append(emp_id)
        else:
            print("Object already exist")

    def show_info(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name : {self.name}")
        print(f"Department : {self.dep}")
        print(f"Monthly Salary : {self.salary}")
        print(f"Yearly Salary : {self.calculate_yearly_salary()}")
        if(self.dep in bonus):
            print(f"Bonus Applied {bonus[self.dep]}% : {self.apply_bonus()}")
        else:
            print(f"Bonus Applied 5% : {self.apply_bonus()}")

    def calculate_yearly_salary(self):
        
        return self.salary*12

    def apply_bonus(self):
        if self.dep in bonus:
            self.salary+=self.salary*(bonus[self.dep]/100)
        else:
            self.salary+=self.salary*0.05
        
        return int(self.salary)
    
emp1 = Employee(101,"Arun Kumar","IT",75000)
emp2 = Employee(102,"Riya Sharma", "HR", 68000)
emp3 = Employee(103,"John Doe", "Finance", 80000)
emp4 = Employee(103,"Arjun","HR",12000)
emp1.show_info()  
emp2.show_info()
emp3.show_info()    

#Output
# Object already exist
# Employee ID : 101
# Name : Arun Kumar
# Department : IT
# Monthly Salary : 75000
# Yearly Salary : 900000
# Bonus Applied 10% : 82500
# Employee ID : 102
# Name : Riya Sharma
# Department : HR
# Monthly Salary : 68000
# Yearly Salary : 816000
# Bonus Applied 8% : 73440
# Employee ID : 103
# Name : John Doe
# Department : Finance
# Monthly Salary : 80000
# Yearly Salary : 960000
# Bonus Applied 12% : 89600