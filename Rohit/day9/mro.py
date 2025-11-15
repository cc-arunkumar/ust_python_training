class Emp:
    def __init__(self):
        pass 
    def perform_task(self):
        print("employee completed the task")
class Manager(Emp):
    def perform_task(self):
        print("Manager completed the task")
class Developer(Emp):
    # def perform_task(self):
       pass
class Tester(Emp):
    def perform_task(self):
        print("Tester completed the task")
        
        
employess = [Emp(),Manager(),Developer(),Tester() ]
for emp in employess:
    emp.perform_task()