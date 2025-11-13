# the code shows how different classes can define the same method name but perform different
# actions when that method is called.

class Employee:
    def work(self):
        print("Employee is working on random task")
    
class Developer:
    def work(self):
        print("developer is coding")

class Manager:
    def work(self):
        print("Managing project on cyber security")
        
e1=Employee()
d1=Developer()
m1=Manager()

e1.work()
d1.work()
m1.work()


# Output
# Employee is working on random task
# developer is coding
# Managing project on cyber security