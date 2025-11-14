# Parent class (Base class)
class Employee:
    # Method that will be overridden by child classes
    def perform_tasks(self):
        print("Employee is working on day to day tasks")


# Child class → Developer
class Developer(Employee):
    # Overriding perform_tasks() method
    def perform_tasks(self):
        print("Developer is developing the code for the given requirement")


# Child class → Manager
class Manager(Employee):
    # Overriding perform_tasks() method
    def perform_tasks(self):
        print("Manager is managing the tasks in Jira")


# Child class → Tester
class Tester(Employee):
    # Overriding perform_tasks() method
    def perform_tasks(self):
        print("Tester is testing the project in Jira")


# Creating objects for each class
emp1 = Employee()
dev1 = Developer()
manager1 = Manager()
test1 = Tester()

# Storing all objects in list → shows polymorphism
employee = [emp1, dev1, manager1, test1]

# Looping and calling same method name → different behavior
for emp in employee:
    emp.perform_tasks()


# Sample Output:
# Employee is working on day to day tasks
# Developer is developing the code for the given requirement
# Manager is managing the tasks in Jira
# Tester is testing the project in Jira