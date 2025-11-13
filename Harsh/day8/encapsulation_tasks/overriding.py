# Parent class
class Employee:
    def work(self):
        print("Employee works on general tasks")

class Developer(Employee):
    def work(self):
        print("Developer works only on coding")

class Manager(Employee):
    def work(self):
        print("Manager works only on planning and meetings")


emp = Employee()
dev = Developer()
mgr = Manager()

emp.work()   
dev.work()   
mgr.work()   



# Employee works on general tasks
# Developer works only on coding
# Manager works only on planning and meetings