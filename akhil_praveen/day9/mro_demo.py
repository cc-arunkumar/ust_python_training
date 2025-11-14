# MRO -  Method resolution order
class Employee:
    def perform_task(self):
        print("Employee perform task.")
        
class Manager(Employee):
    def perform_task(self):
        print("Manager perform task.")
        
class Developers(Employee):
    pass
        

class Tester(Employee):
    def perform_task(self):
        print("Teaster perform task.")
  
        
emp1 = Employee()

dev1 = Developers()

man1 = Manager()

test1 = Tester()

service_req = [emp1,man1,dev1,test1]

for i in service_req:
    i.perform_task()
    
# Output
# Employee perform task.
# Manager perform task. 
# Employee perform task.
# Teaster perform task. 