# Method resolution order
class Employee():
    
    def perform_task(self):
        print("The employee performs a daily task")
class Manager(Employee):
    def perform_task(self):
        print("The manager assign the tasks to employees")
class Developers(Employee):
   def perform_task(self):
      print("the developer performed on coding task ")
class Tester(Employee):
    # def perform_task(self):
    #     # print("The tester evaluate the code")
        pass

employee=[Employee(),Manager(),Developers(),Tester()]
for emp in employee:
    
    emp.perform_task()
# sample output
# The employee performs a daily task
# The manager assign the tasks to employees
# the developer performed on coding task
# The employee performs a daily task