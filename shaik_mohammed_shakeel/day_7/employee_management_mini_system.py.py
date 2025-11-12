class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee department: {self.department}")
        print(f"Employee Salary: {self.salary}")

    def calculate_yearly_salary(self):
        return self.salary*12
    
    def apply_bonus(self):
        if(self.department=="IT"):
            self.salary+=self.salary*0.10
            print(f"Bonus Applied (10%): {self.salary} ")
        elif(self.department=="HR"):
            self.salary+=self.salary*0.08
            print(f"Bonus Applied (8%): {self.salary} ")
        elif(self.department=="Finance"):
            self.salary+=self.salary*0.12
            print(f"Bonus Applied (12%): {self.salary} ")
        else:
            self.salary+=self.salary*0.05
            print(f"Bonus Applied (5%): {self.salary} ")

emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)
 

emp1.show_info()
print(f"Yearly Salary: {emp1.calculate_yearly_salary()}")
emp1.apply_bonus()
print("---------------------")

emp2.show_info()
print(f"Yearly Salary: {emp2.calculate_yearly_salary()}")
emp2.apply_bonus()
print("---------------------")


emp3.show_info()
print(f"Yearly Salary: {emp3.calculate_yearly_salary()}")
emp3.apply_bonus()
print("---------------------")






        