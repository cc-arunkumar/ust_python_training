class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
        
    def show_info(self):
        print(f"Employee ID:",self.emp_id)
        print(f"Name:",self.name)
        print(f"Department:",self.department)
        print(f"Salary:",self.salary)
        
    def calculate_yearly_salary(self):
        yearly_salary = self.salary*12
        print(f"yearly salary of {self.name} is {yearly_salary} ")        

    def apply_bonus(self):
        if self.department=='IT':
           new_salary = self.salary + self.salary*0.10
           print("after bonus",new_salary) 
        elif self.department=='HR':
           new_salary = self.salary+self.salary*0.08
           print("after bonus",new_salary) 
        elif self.department == 'Finance':
            new_salary=self.salary+self.salary*0.12
            print("after bonus",new_salary) 
        else:
            new_salary=self.salary+self.salary*0.05
            print("after bonus",new_salary) 

emp1=Employee(101,"Taniya","IT",50000)
emp2=Employee(102,"Amit","IT",60000)             
emp3=Employee(103,"Riya","Finance",40000)             
emp4=Employee(104,"Sonia","HR",70000)
print("Employee1")
emp1.show_info() 
emp1.calculate_yearly_salary()
emp1.apply_bonus() 
print(" ")
print("Employee2")
emp2.show_info()
emp2.calculate_yearly_salary() 
emp2.apply_bonus()
print(" ")
print("Employee3")
emp3.show_info()
emp3.calculate_yearly_salary() 
emp3.apply_bonus()
print(" ")
print("Employee4")
emp4.show_info()
emp4.calculate_yearly_salary() 
emp4.apply_bonus()


# output
# Employee1
# Employee ID: 101
# Name: Taniya    
# Department: IT  
# Salary: 50000   
# yearly salary of Taniya is 600000
# after bonus 55000.0

# Employee2
# Employee ID: 102
# Name: Amit
# Department: IT
# Salary: 60000
# yearly salary of Amit is 720000
# after bonus 66000.0

# Employee3
# Employee ID: 103
# Name: Riya
# Department: Finance
# Salary: 40000
# yearly salary of Riya is 480000
# after bonus 44800.0

# Employee4
# Employee ID: 104
# Name: Sonia
# Department: HR
# Salary: 70000
# yearly salary of Sonia is 840000
# after bonus 75600.0

         
        