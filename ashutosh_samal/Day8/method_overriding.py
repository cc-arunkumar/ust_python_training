#Method overriding
#Employee class creation
class Employee:
    def work(self):
        print("Employee is doing day to day task")

#class developer inherited from employee
class Developer(Employee):
    def work(self):
        print("Developer is writing code")

#class manager inherited from employee
class Manager(Employee):
    def work(self):
        print("Manager is managing different projects")

#object creation and function calling
e1 = Employee()
e1.work()

e2 = Developer()
e2.work()

e3 = Manager()
e3.work()

#Sample Execution
# Employee is doing day to day task
# Developer is writing code
# Manager is managing different projects