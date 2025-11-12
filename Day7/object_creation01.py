class emp:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def promotion(self,increment,salary):
        self.salary += (salary*increment)
        print(f"{self.name} has been promoted ! New salary is {self.salary}")

emp1 = emp("madhan",22,30000)
emp2 = emp("madhan",22,30000)

print(f"Employee name:{emp1.name}")
print(f"Employee name:{emp1.salary}")
print(f"Employee name:{emp1.age}")
promo = emp1.promotion(0.10,30000)

# sample output:
# Employee name:madhan
# Employee name:30000
# Employee name:22
# madhan has been promoted ! New salary is 33000.0