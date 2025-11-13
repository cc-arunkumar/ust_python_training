# method over raiding
class Employee:
    def work(self):
        print("thw Employee is working in the project")
class Developer(Employee):
    def work(self):
        print("the developer is on project ")
class Manager(Employee):
    def work(self):
        print("the manager is managing the team ")

c1=Employee()
c2=Developer()
c3=Manager()
c1.work()
c2.work()
c3.work()

# output
# thw Employee is working in the project
# the developer is on project 
# the manager is managing the team
