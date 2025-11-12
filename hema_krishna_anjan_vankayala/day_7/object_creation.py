# Simple Employee class with id, name and salary
class Emp:
    def __init__(self,id,name,salary):
        self.id = id 
        self.name = name
        self.salary = salary 
    
    def promote(self,increment):
        self.salary += increment
        print("New Salary is ", self.salary)

# create an Emp instance and demonstrate promote()
emp1 = Emp(101,"Rahul",50000)
emp1.promote(5000)

print("Employee ID:", emp1.id)
print("Employee Name:", emp1.name)
print("Employee Salary:", emp1.salary)

# Developer inherits from Emp
class Developer(Emp):
    def __init__(self,programming_lang_list : list[str]):
        self.program_list = programming_lang_list

emp1 = Emp(101,"Rahul",50000)
dev1 = Developer(103,"Raul",6000,["Python","Java","C++"])


#Sample Output 
# New Salary is  55000
# Employee ID: 101
# Employee Name: Rahul
# Employee Salary: 55000