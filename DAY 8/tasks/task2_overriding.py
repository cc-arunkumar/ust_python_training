class Employee:
    def __init__(self):
        pass
    def work(self):
        print("Employee is working")
        
#Inheritance
class Developer(Employee):
    def work(self):
        print("Developer is working")

#Inheritance
class Manager(Employee):
    def drop(self):
        print("Manager is working")

e1=Employee()
e1.work()

d1=Developer()
d1.work()

m1=Manager()
m1.work()

"""
SAMPLE OUTPUT

Employee is working
Developer is working
Employee is working
"""

# No work() method in Manager class. So, Parent class object is called