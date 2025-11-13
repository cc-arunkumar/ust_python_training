# method overriding
class Employee:
    def work(self):
        print("Employee is working on generic day to day task")
class Developer(Employee):
    def work(self):
        print("Developer is coding the requirement")
class Manager(Employee):
    def work(self):
        print("Managing project Modules")
e1=Employee()
d1=Developer()
m1=Manager()

e1.work()
d1.work()
m1.work()

# sample output

# Employee is working on generic day to day task
# Developer is coding the requirement
# Managing project Modules

