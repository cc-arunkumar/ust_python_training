#Creating class
class Emp:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    #function to promote and increase salary
    def promote(self,increment):
        self.salary += increment
        print(f"{self.name} has been promoted! New salary is {self.salary}")

#Creating an object
emp1 = Emp("Amit",30,50000)
emp2 = Emp("Sonia",28,60000)

#Displaying initial details
print(f"Employee Name: {emp1.name}")
print(f"Employee Age: {emp1.age}")
print(f"Employee Salary: {emp1.salary}")
print(f"Employee Name: {emp2.name}")
print(f"Employee Age: {emp2.age}")
print(f"Employee Salary: {emp2.salary}")


#Sample Output
# Employee Name: Amit
# Employee Age: 30
# Employee Salary: 50000
# Employee Name: Sonia
# Employee Age: 28
# Employee Salary: 60000