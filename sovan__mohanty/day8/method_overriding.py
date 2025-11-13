class Employee:
    def work(self):
        print("Employee is working on a generic day to day task")
class Developer(Employee):
    def work(self):
        print("Developer is coding the requirement given")
class Manager(Employee):
        def work(self):
            print("Managing project module progress in Jira on daily basis")
e1=Employee()
d1=Developer()
m1=Manager()

e1.work()
d1.work()
m1.work()

#Sample Execution
# Employee is working on a generic day to day task
# Developer is coding the requirement given
# Managing project module progress in Jira on daily basis