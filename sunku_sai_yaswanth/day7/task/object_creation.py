class emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def promot(self):
        self.salary += (self.salary*0.5)
        return self.salary

emp1=emp(101,"sai",50000)
emp2=emp(102,"neveen",45000)

print(f"emp id: {emp1.id}")
print(f"emp name: {emp1.name}")
print(f"emp sal: {emp1.salary}")
print(f"emp id: {emp2.id}")
print(f"emp name: {emp2.name}")
print(f"emp sal: {emp2.salary}")

emp1.promot()
print(f"the emp1 salary is:{emp1.salary}")
