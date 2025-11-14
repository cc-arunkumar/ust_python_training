#Task  : Method Resolution Order 



class Employee():
    def perform_task(self):
        print("Employee calling ")
        
class Developer(Employee):
        pass

class Manager(Employee):
    def perform_task(self):
        print(f"Attending meetings")

class Tester(Employee):
    def perform_task(self):
        print(f"Testing a code ")
        

employees=[Employee(),Manager(),Developer(),Tester()]

for emp in employees:
    emp.perform_task()
    
#Output
# Employee calling 
# Attending meetings
# Employee calling  
# Testing a code

    