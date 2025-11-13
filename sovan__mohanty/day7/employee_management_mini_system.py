#Task Employee Management Mini System

#Creating a class name Employee
class Employee:
    #Initializing it using init function
    def __init__(self,empid,name,dept,sal):
        self.empid=empid
        self.name=name
        self.dept=dept
        self.sal=sal
    #creating function to display employee details
    def show_info(self):
        print(f"Employee id: {self.empid}")
        print(f"Employee name: {self.name}")
        print(f"Employee department: {self.dept}")
        print(f"Employee salary: Rs {self.sal}")
    
    #Creating a function which calculates the yearly salary
    def calculate_yearly_salary(self):
        return (self.sal*12)
    
    #Creating a function which applies bonus
    def apply_bonus(self):
        if(self.dept.upper()=="IT"):
            bonus=self.sal+(self.sal*0.10)
            return(bonus)
        elif(self.dept.upper()=="HR"):
            bonus=self.sal+(self.sal*0.08)
            return(bonus)
        elif(self.dept.upper()=="Finance".upper()):
            bonus=self.sal+(self.sal*0.12)
            return(bonus)
        else:
            bonus=self.sal+(self.sal*0.05)
            return(bonus)
#Object creation and value initialization
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)
emp1.show_info()
print(f"Yearly Salary:  Rs {emp1.calculate_yearly_salary()}")
print(f"Bonus Applied (10%):  Rs {emp1.apply_bonus()}")
print("======================================================")
emp2.show_info()
print(f"Yearly Salary:  Rs {emp2.calculate_yearly_salary()}")
print(f"Bonus Applied (8%):  Rs {emp2.apply_bonus()}")
print("======================================================")
emp3.show_info()
print(f"Yearly Salary:  Rs {emp3.calculate_yearly_salary()}")
print(f"Bonus Applied (12%) :  Rs {emp3.apply_bonus()}")

#Sample Execution
# Employee id: 101
# Employee name: Arun Kumar
# Employee department: IT
# Employee salary: Rs 75000
# Yearly Salary:  Rs 900000
# Bonus Applied (10%):  Rs 82500.0
# ======================================================
# Employee id: 102
# Employee name: Riya Sharma
# Employee department: HR
# Employee salary: Rs 68000
# Yearly Salary:  Rs 816000
# Bonus Applied (8%):  Rs 73440.0
# ======================================================
# Employee id: 103
# Employee name: John Doe
# Employee department: Finance
# Employee salary: Rs 80000
# Yearly Salary:  Rs 960000
# Bonus Applied (12%) :  Rs 89600.0
    