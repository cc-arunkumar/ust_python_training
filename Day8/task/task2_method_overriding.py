class Employee:
    def __init__(self):
        pass
    def work(self):
        print("Employee is working")
#Inheritance
class Developer(Employee):
    def work(self):
        print("Developer is working")

class Manager(Employee):
    def over(self):
        print("Manager is working")

e1=Employee()
e1.work()

d1=Developer()
d1.work()

m1=Manager()
m1.over()

# sample output:
# Employee is working
# Developer is working
# Manager is working

