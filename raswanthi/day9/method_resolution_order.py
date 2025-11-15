#Method Resolution task

class Employee:
    def perform_task(self):
        print("Performing Tasks")
        
class Developer(Employee):
        
    def perform_task(self):
        print("developing the code")
        print("executing code")
        
class Manager(Employee):
        
    def perform_task(self):
        pass 
    
class Tester(Employee):
    def perform_task(self):
        print("Raising error")
   
employees=[Employee(),Manager(),Developer(),Tester()]   #Grouping every class in a list called 'employees'

for emp in employees:
    emp.perform_task()   #For-loop for performing tasks for every class in the 'employees' list
    

'''
output:
{'id': 'E01', 'name': 'Nisha', 'dept': 'IT'}
pt': 'IT', 'platform': 'Python-Fullstack', 'technology': 'React'}
{'id': 'E04', 'name': 'Jery', 'dept': 'IT', 'platform': 'Python-fullstack', 'languge': 'Python'}
'''
