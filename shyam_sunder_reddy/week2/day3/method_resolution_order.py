#Parent class 
class Employee:
    def perform_task(self):
        print("Marking the attendence")

#child class of the employee
class Manager(Employee):
    def perform_task(self):
        print("Taking updates from the team")

#child class of the employee
class Developer(Employee):
    def perform_task(self):
        print("Developing the web page")
    
#child class of the employee
class Tester(Employee):
    pass
    # def perform_task(self):
    #     pass
        #print("throwing the bugs")
#output
#throwing the bugs
    
#creating the objects
e1=Employee()
m1=Manager()
d1=Developer()
t1=Tester()

emploees=[e1,m1,d1,t1,Employee(),Manager(),Developer(),Tester()]
for emp in emploees:
    emp.perform_task()


#Sample output
# Marking the attendence
# Taking updates from the team
# Developing the web page
# Marking the attendence
# Marking the attendence
# Taking updates from the team
# Developing the web page
# Marking the attendence