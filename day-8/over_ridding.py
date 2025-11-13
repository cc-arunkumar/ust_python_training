#implementing over ridding

class Employee:
    def work(self):
        print("Employee is working on random task")
        
class Developer:  
    def work(self):
        print("developer is coding")
        
class Manager:
    def work(self):
        print("Managing project on cyber proof")
        
e1=Employee()
d1=Developer()
m1=Manager()

e1.work()
d1.work()
m1.work()


#o/p:
# Employee is working on random task
# developer is coding
# Managing project on cyber proof