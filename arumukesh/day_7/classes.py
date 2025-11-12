class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def promote(self,increment):
        self.salary+=(increment/100)* self.salary
        return self.salary

emp1=Emp("Arjun",34,23000)
emp2=Emp("arthi",33,45000)
print(emp1.name,emp1.salary)
# incrementing the salaries by 10%
emp1.promote(10)
print(emp1.salary)