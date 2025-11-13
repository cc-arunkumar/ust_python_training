class Employee:
    def __init__(self):
        self.name="arumukesh"
        self._designation="HR"
        self.__salary=50000
    def get_salary(self):
        print(f"Salary of {self.name} is {self.__salary}")
    def showdetails(self):
        print(self.name,self._designation,self.__salary)

    def set_salary(self,amount):
        self.__salary=amount
        print(f"employee salary updated to {amount}")


    

emp1=Employee()
print("printing employee details")
emp1.showdetails()
print("printing name and designation")
print(emp1.name)
print(emp1._designation)
emp1.set_salary(50000)
print(emp1._Employee__salary)
emp1.set_salary(50000)
print(emp1.__dict__)
try:
    print(emp1.__salary)
except AttributeError:
    print("Private variable not accessible")

# printing employee details
# arumukesh HR 50000
# printing name and designation
# arumukesh
# HR
# employee salary updated to 50000
# 50000
# employee salary updated to 50000
# {'name': 'arumukesh', '_designation': 'HR', '_Employee__salary': 50000}
# Private variable not accessible