class Employee:
    def __init__(self,name,department):
        self.name=name # public
        self._department=department #protected
        self.__salary=0 # private
        # self.__salary=salary

    #setter 
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else : print("Enter salary Gretaer than 0")

    def get_salary(self):
        return self.__salary
    
    def show_info(self):
        print("Name :",self.name)
        print("Department :",self._department)
        # print("Salary :",self.__salary)

e1=Employee("Gowtham","IT")
e1.set_salary(10000)
e1.show_info()
# print(e1._Employee__salary)
print(e1.__salary) # direct access slary
print("Accessing salary using getter",e1.get_salary()) # access salary using getter
    
"""
SAMPLE OUTPUT

 # accessing salary directly
Name : Gowtham
Department : IT

AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?


Name : Gowtham
Department : IT
Accessing salary using getter 10000

"""
