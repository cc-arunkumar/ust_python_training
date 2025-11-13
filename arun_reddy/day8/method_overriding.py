class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    
    def work(self):
        print("Developer is developeoing teh code given")
    
    
class Manager(Employee):
    def work(self):
        print("Manager manages the work ")



emp1=Employee()
dev1=Developer()
man1=Manager()
emp1.work()
dev1.work()
man1.work()
# sample execution 
# Employee is working
# Developer is developeoing teh code given
# Manager manages the work 