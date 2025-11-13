# Method overriding

class Employee:
    def work(self):
        print("Employee is working on day to day task")
    
class Developer(Employee):
    def work(self):
        print("Developer is developing the code for given requirement ")

class Manager(Employee):
    def work(self):
        print("Manager is managing the task in jira")

emp1=Employee()
dev1=Developer()
manager1=Manager()

# Method overriding with same method name but different body
emp1.work()
dev1.work()
manager1.work()

# sample output
# Employee is working on day to day task
# Developer is developing the code for given requirement 
# Manager is managing the task in jira