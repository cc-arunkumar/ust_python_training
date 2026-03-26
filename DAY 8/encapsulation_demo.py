class Employee:

    def __init__(self):
        self.name="Gowtham"
        self._designation="SDE 1"
        self.__salary=30000
    
    #function call
    def show_emp_details(self):
        print("Name :",self.name)
        print("Designation :",self._designation)
        print("Salary :",self.__salary)


e1=Employee()
e1.show_emp_details()

# print("Name :",e1.name)
# print("Designation :",e1._designation)
# print("Salary :",e1._Employee__salary)

print("Salary :",e1._Employee__salary)

"""
SAMPLE OUTPUT

Name : Gowtham
Designation : SDE 1
Salary : 30000
Salary : 30000 -> CALLING SEPERATELY
"""