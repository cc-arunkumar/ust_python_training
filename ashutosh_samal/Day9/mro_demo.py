#Method Resolution Order

#creating parent class
class Employee:
    def perform_task(self):
        print("working")

#creating child class
class Manager(Employee):
    def perform_task(self):
        print("Managing different projects")

#creating child class
class Developer(Employee):
    pass
    # def perform_task(self):
    #     print("Writing codes")

#creating child class
class Tester(Employee):
    def perform_task(self):
        print("Reporting bugs")

#object creation        
m1 =Manager()
d1 = Developer()
t1 =Tester()

#list to store object
employee =[m1,d1,t1]

#loop to iterate the list and calling the function
for emp in employee:
    emp.perform_task()
    
    
#Sample Execution
# Managing different projects
# working
# Reporting bugs