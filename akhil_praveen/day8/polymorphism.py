class Employee:
    def work(self):
        print("Employee is working")
        
class Developer(Employee):
    
    def work(self):
        print("Developer is working")
        
class Manager(Employee):
    
    def work(self):
        print("Manager is working")
        
e1 = Employee()
d1 = Developer()
m1 = Manager()

e1.work()
d1.work()
m1.work()