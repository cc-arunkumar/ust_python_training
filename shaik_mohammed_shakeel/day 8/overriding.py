#Overriding

class Employee:
    def work(self):
        print("Employee is doing daily tasks")
class Developer(Employee):
    def work(self):
        print("Developer is working on project")
class Manager(Employee):
    def work(self):
        print("Manager is managing the projects")

e1=Employee()
d1=Developer()
m1=Manager()

e1.work()
d1.work()
m1.work()