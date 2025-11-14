# method resolution order

class Employee:
    def perform_task(self):
        print("the task is started performing")
class Manager(Employee):
    def perform_task(self):
        print("the task of the marager is to manage thework")
class Developer(Employee):
    # def perform_task(self):
        pass
class Tester(Employee):
    def perform_task(self):
        print("the tester is testing the code and raising the bugs")
        
e1=Manager()
e2=Developer()
e3=Tester()
        
emp=[e1,e2,e3]

for employee in emp:
    employee.perform_task()

# output
# the task of the marager is to manage thework
# the task is started performing
# the tester is testing the code and raising the bugs