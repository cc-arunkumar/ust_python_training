# #Method Resolution Order
# 1.Check the currrent executing Object 
# 2.If not Found check its parent 
# 3.Untill Top most in Inheritance
# 4.If not found throw error 
class Employee:
    def perform_task(self):
        print("Task of Employee")
        
class Developer(Employee):
    def perform_task(self):
        print("Task of Developer")

class Manager(Employee):
    pass 

dev = Developer()
manager = Manager()
li = [dev,manager]
for emp in li:
    emp.perform_task()
# dev.perform_task() #returns the Developer object's method
# manager.perform_task() #returns the Employee(Parent) object's method 

#Sample Output 
# Task of Developer
# Task of Employee
        