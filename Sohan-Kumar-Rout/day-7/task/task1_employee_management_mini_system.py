#Task 1 : Employee Management Mini System

#Code
class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
    def show_info(self):
        print(f"Employee id : {self.emp_id} ")
        print(f"Employee name : {self.name}")
        print(f"Employee department : {self.department}")
        print(f"Employee salary : {self.salary}")
    def calculate_yearly_salary(self):
        return (self.salary * 12)
    
    def apply_bonus(self):
        
        bonus=0
        if self.department.lower()=="it":
            bonus=self.salary * 0.10
        elif self.department.lower()=="hr":
            bonus=self.salary * 0.08
        elif self.department.lower()=="finance":
            bonus=self.salary * 0.12
        else:
            bonus=self.salary * 0.05
        
        bonus_amt=self.salary + bonus
        self.salary+=bonus_amt
        return bonus_amt
emp1=Employee(101,"Arun Kumar","IT",75000)
emp2=Employee(102,"Riya Sharma","HR",68000)
emp3=Employee(103,"John Doe","Finance",80000)
emp1.show_info()
print(f"Yearly salary : {emp1.calculate_yearly_salary()}")
print(f"Calculate Bonus {emp1.apply_bonus()}")
print("==================================================")

emp2.show_info()
print(f"Yearly salary : {emp2.calculate_yearly_salary()}")
print(f"Calculate Bonus {emp2.apply_bonus()}")
print("==================================================")

emp3.show_info()
print(f"Yearly salary : {emp3.calculate_yearly_salary()}")
print(f"Calculate Bonus {emp3.apply_bonus()}")
print("==================================================")


#Output
# Employee id : 101 
# Employee name : Arun Kumar
# Employee department : IT
# Employee salary : 75000
# Yearly salary : 900000
# Calculate Bonus 82500.0
# ==================================================
# Employee id : 102 
# Employee name : Riya Sharma
# Employee department : HR
# Employee salary : 68000
# Yearly salary : 816000
# Calculate Bonus 73440.0
# ==================================================
# Employee id : 103
# Employee name : John Doe
# Employee department : Finance
# Employee salary : 80000
# Yearly salary : 960000
# Calculate Bonus 89600.0
# ==================================================  
        
    
    