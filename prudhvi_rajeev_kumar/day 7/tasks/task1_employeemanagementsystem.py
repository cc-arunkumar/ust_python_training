class Employee:
    def __init__(self, empid, name, dept, salary):
        self.empid = empid
        self.name = name
        self.dept = dept
        self.salary = salary

#Task 1 :
    def show_info(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee ID : {self.empid}")
        print(f"Employee Department : {self.dept}")
        print(f"Employee Monthly salary : {self.salary}")
    
#Task 2:
    def calculate_yearly_salary(self):
        yearly_salary = self.salary * 12
        print(f"Yearly salary : {yearly_salary}")

#Task 3:
    def apply_bonus(self):
        if self.dept == "IT":
            bonus = (self.salary * 0.1) + self.salary
            print(f"Bonus Applied : {bonus}")
        elif self.dept == "HR":
            bonus = (self.salary * 0.08) + self.salary
            print(f"Bonus Applied : {bonus}")
        elif self.dept == "Finance":
            bonus = (self.salary * 0.12) + self.salary
            print(f"Bonus Applied : {bonus}")
        else:
            bonus = (self.salary * 0.05) + self.salary
            print(f"Bonus Applied : {bonus}")


print("----------------------------------------")
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp1.show_info()
emp1.calculate_yearly_salary()
emp1.apply_bonus()
print("-----------------------------------------")
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp2.show_info()
emp2.calculate_yearly_salary()
emp2.apply_bonus()
print("------------------------------------------")
emp3 = Employee(103, "John Doe", "Finance", 80000)
emp3.show_info()
emp3.calculate_yearly_salary()
emp3.apply_bonus()

#Console Output:
# ----------------------------------------
# Employee Name : Arun Kumar
# Employee ID : 101
# Employee Department : IT
# Employee Monthly salary : 75000
# Yearly salary : 900000
# Bonus Applied : 82500.0
# -----------------------------------------
# Employee Name : Riya Sharma
# Employee ID : 102
# Employee Department : HR
# Employee Monthly salary : 68000
# Yearly salary : 816000
# Bonus Applied : 73440.0
# -----------------------------------------
# Employee Name : John Doe
# Employee ID : 103
# Employee Department : Finance
# Employee Monthly salary : 80000
# Yearly salary : 960000
# Bonus Applied : 89600.0








    