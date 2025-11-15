# Method Resolution Order

class Employee:
    def perform_task(self):
        print("Employee is working on day to day task")
    
class Developer(Employee):
    def perform_task(self):
        print("Developer is developing the code for given requirement ")

class Manager(Employee):
    def perform_task(self):
        print("Manager is managing the task in jira")

class Tester(Employee):
    pass
    # def perform_task(self):
    #     print("Tester is testing the code")

emp1=Employee()
dev1=Developer()
manager1=Manager()
test1=Tester()


employees=[emp1,dev1,manager1,test1]

for emp in employees:
    emp.perform_task()
    print("           ")

# Sample output

# EEmployee is working on day to day task

# Developer is developing the code for given requirement 

# Manager is managing the task in jira

# Employee is working on day to day task