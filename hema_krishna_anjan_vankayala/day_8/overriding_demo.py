class Employee:
    def work(self):
        print("Working on generic task")

class Developer:
    def work(self):
        print("Developer is working on the project")

class Manager:
    def work(self):
        print("Manager is managing the flow of project in Jira")

d1 = Employee()
d2= Developer()
d3 = Manager()
d1.work()
d2.work()
d3.work()
 
 
 #Sample Output 
# Working on generic task
# Developer is working on the project
# Manager is managing the flow of project in Jira