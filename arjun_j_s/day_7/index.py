class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def promote(self,increment_amt):
        self.salary+=increment_amt
    
emp1 = Employee("Arjun",23,30000)
emp2 = Employee("Rahul",23,40000)

emp1.promote(11000)

print("Employee 1 name",emp1.name)
print("Employee 1 age",emp1.age)
print("Employee 1 salary",emp1.salary)

print("Employee 2 name",emp2.name)
print("Employee 2 age",emp2.age)
print("Employee 2 salary",emp2.salary)