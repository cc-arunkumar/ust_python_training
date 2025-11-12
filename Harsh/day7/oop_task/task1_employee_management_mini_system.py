class Employee:
    def __init__(self,emp_id,name,dept,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
        self.dept=dept
    
    def show_info(self):
        print(f"Employee emp_id:{self.emp_id}")
        print(f"Employee name:{self.name}")
        print(f"Employee department:{self.dept}")
        print(f"Monthly salary:{self.salary}")
       
    def monthly_salary(self):
        return self.salary
        
    def calculate_yearly_salary(self):
        return (self.salary)*12
    
    def apply_bonus(self):
        if self.dept=="IT":
            bonus= self.salary + (self.salary*0.10)
            return bonus
        if self.dept=="HR":
            bonus= self.salary + (self.salary*0.08)
            return bonus
        if self.dept=="Finance":
            bonus= self.salary + (self.salary*0.12)
            return bonus
        else:
            bonus= self.salary + (self.salary*0.05)
            return bonus
        
        
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)
emp1.show_info()
print("Yearly salary:",emp1.calculate_yearly_salary())
print("Bonus Applied (10%):",emp1.apply_bonus())

print("------------------------------------------------")
emp2.show_info()
print("Yearly salary:",emp2.calculate_yearly_salary())
print("Bonus Applied (8%):",emp2.apply_bonus())

print("------------------------------------------------")

emp3.show_info()
print("Yearly salary:",emp3.calculate_yearly_salary())
print("Bonus Applied (12%):",emp3.apply_bonus())



# Employee emp_id:101
# Employee name:Arun Kumar
# Employee department:IT
# Monthly salary:75000
# Yearly salary: 900000
# Bonus Applied (10%): 82500.0
# ------------------------------------------------
# Employee emp_id:102
# Employee name:Riya Sharma
# Employee department:HR
# Monthly salary:68000
# Yearly salary: 816000
# Bonus Applied (8%): 73440.0
# ------------------------------------------------
# Employee emp_id:103
# Employee name:John Doe
# Employee department:Finance
# Monthly salary:80000
# Yearly salary: 960000
# Bonus Applied (12%): 89600.0