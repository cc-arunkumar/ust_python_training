# method_resolution_order
class Employee():
    def perform_task(self):
        print("parent Employee")
    
    
class Manager(Employee):
    def perform_task(self):
        print("Managing the task")
    
        
class developer(Employee):
    pass


class Tester(Employee):
    def perform_task(self):
        print("debugging a task")
    
m1=Manager()
m1.perform_task()
d1=developer()
d1.perform_task()

# sample output
# Managing the task
# dev a project


# when pass is provided:
# Managing the task
# parent Employee


