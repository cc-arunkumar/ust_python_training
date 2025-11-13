class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):  
        print("Developer is writing code")


class Manager(Employee):
    def work(self):  
        print("Manager is managing the team")

# Usage
emp = Employee()
emp.work()      

dev = Developer()
dev.work()      

mgr = Manager()
mgr.work()     
