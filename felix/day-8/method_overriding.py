class Employee:
    def work(self):
        print("Employee is working")
        
class Dveloper(Employee):
    def work(self):
        print("Developer is developing a software")
        
class Manager(Employee):
    def work(self):
        print("Manager is managing tasks")
        
# Creating objects for all classes
emp = Employee()
dev = Dveloper()
man = Manager()

# Calling overridden methods
emp.work()
dev.work()
man.work()

# output

# Employee is working
# Developer is developing a software
# Manager is managing tasks