#The object creation demo
#employee class
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def promotion(self,increment):
        self.salary +=increment
        print(f"Salary incremented Rs.{increment} for {self.name}")

#taking input
name=input("Enter Employee Name: ")
age=int(input("ENter Employee age: "))
salary=int(input("Enter Employee Salary: "))
emp1=Employee(name,age,salary)



print(f"Employee Name:{emp1.name}")
print(f"Employee age:{emp1.age}")
print(f"Employee Salary:{emp1.salary}")

#output
# Enter Employee Name: Bhargavi S
# ENter Employee age: 12
# Enter Employee Salary: 3000
# Employee Name:Bhargavi S
# Employee age:12

# Employee Salary:3000
