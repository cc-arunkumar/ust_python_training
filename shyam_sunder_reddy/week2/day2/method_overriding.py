class Employee:
    def work(self):
        print("Working on som generic task")

class Developer:
    def work(self):
        print("Developer is working on the project")
        
class Manager:
    def work(self):
        print("Manager is managing the flow of the project")
    
e1=Employee()
d1=Developer()
m1=Manager()

e1.work()
d1.work()
m1.work()

#Sample output
# Working on som generic task
# Developer is working on the project
# Manager is managing the flow of the project