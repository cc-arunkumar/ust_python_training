#Method Resolution order - if child class does not have any function it will call parent class

#Defining parent class
class Employee:
    def perform_task(self):
        print("Employee is working 24/7")


#subclass
class Manager(Employee):
    #overrided function
    def perform_task(self):
        print("Manager is managing the developers and testers")
        

#subclass
class Developer(Employee):
    #overrided function
    def perform_task(self):
        print("Developer is vibe coding")
        
        
#subclass
class Tester(Employee):
    #overrided function
    # def perform_task(self):
    #     print("Tester is raising bugs and annoying developers")
    pass
    #This will call the parent class method


employees=[Manager(),Developer(),Tester()]

for i in employees:
    i.perform_task()
    print("----------------------------")
        


#Sample output

# Manager is managing the developers and testers
# ----------------------------
# Developer is vibe coding
# ----------------------------
# Employee is working 24/7
# ----------------------------