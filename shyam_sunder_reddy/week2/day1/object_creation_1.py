class Emp:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def promote(self,increment):
        self.salary+=increment
        print(f"{self.name} has been incremented to {self.salary}")

#creating an object
emp1=Emp("shyam",21,425000)
emp2=Emp("Ram",21,260000)

#Displaying intial details
print("name: ",emp1.name)
print("age: ",emp1.age)
print("salary: ",emp1.salary)
print("name: ",emp2.name)
print("age: ",emp2.age)
print("salary: ",emp2.salary)

# promoting employees with increments
emp1.promote(2000)
emp2.promote(1000)

#Sample Output
# name:  shyam
# age:  21
# salary:  425000
# name:  Ram
# age:  21
# salary:  260000
# shyam has been incremented to 427000
# Ram has been incremented to 261000