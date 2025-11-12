class Emp:
    def __init__(self,name,id,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} has been promoted! now his salary is {self.salary}")

# Create an object of the Emp class
emp1=Emp("Niranjan",22,30000)
emp2=Emp("sai",21,25000)

# Display Details

print(f"Employee Name:{emp1.name}")
print(f"Employee id:{emp1.id}")
print(f"Employee Salary:{emp1.salary}")
print(f"Employee Name:{emp2.name}")
print(f"Employee id:{emp2.id}")
print(f"Employee Salary:{emp2.salary}")

emp1.promote(10000)
        

# Sample output
# Employee Name:Niranjan
# Employee id:22
# Employee Salary:30000
# Employee Name:sai
# Employee id:21
# Employee Salary:25000
# Niranjan has been promoted! now his salary is 40000