# Employee Management Mini
# System
# Objective:
# Learn how to define a class, create multiple objects, and interact with them — just
# like how HR systems track employees in a company.
# Scenario:
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
# Apply a bonus based on departmen



#Initialising variable
class Employee:
    #initialising constructor
    
    def __init__(self,emp_id,name,dept,salary):
        #initialising instance variables
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary
    #defining a function to display the employee info

    
    def show_info(self):
        print(f"Employee ID :{self.emp_id}")
        print(f"Name :{self.name}")
        print(f"Department :{self.dept}")
        print(f"Monthly Salary :₹{self.salary}")
        print(f"Yearly Salary :₹{self.yearly_salary()}")
        #calling the bonus function within here to optimise
        a,b=self.apply_bonus()
        #a and b are variables that stores returned function which is list
        print(f"Bonus Applied ({b}%):₹{a}")
        print("-------------------------------------------") 
        
    def yearly_salary(self):
        #returning salary *12 
        return self.salary*12 
    
    def apply_bonus(self):
        #condition for IT dept
        if self.dept=="IT":
            bonus=10
            self.salary+=(self.salary*bonus)/100
            #returning as a list
            return [round(self.salary),bonus]
        #condition for HR dept
        
        elif self.dept=="HR":
            bonus=8
            self.salary+=(self.salary*bonus)/100
            #returning as a list
            return [round(self.salary),bonus]
        
        #condition for Finance dept
        elif self.dept=="Finance":
            bonus=12
            self.salary+=(self.salary*bonus)/100
            #returning as a list
            return [round(self.salary),bonus]
        #condition for Others
        else:
            bonus=5
            self.salary+=(self.salary*bonus)
            #returning as a list
            return [round(self.salary),bonus]
        
#creation of object
emp1=Employee(101, "Arun Kumar", "IT", 75000)
emp2=Employee(102, "Riya Sharma", "HR", 68000)
emp3=Employee(103, "John Doe", "Finance", 80000)        
emp1.show_info()
emp2.show_info()
emp3.show_info()



#Sample output

# Employee ID :101
# Name :Arun Kumar
# Department :IT
# Monthly Salary :₹75000
# Yearly Salary :₹900000
# Bonus Applied (10%):₹82500
# -------------------------------------------
# Employee ID :102
# Name :Riya Sharma
# Department :HR
# Monthly Salary :₹68000
# Yearly Salary :₹816000
# Bonus Applied (8%):₹73440
# -------------------------------------------
# Employee ID :103
# Name :John Doe
# Department :Finance
# Monthly Salary :₹80000
# Yearly Salary :₹960000
# Bonus Applied (12%):₹89600
# -------------------------------------------