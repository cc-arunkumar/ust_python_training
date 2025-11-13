# Step 1: Define the base class Employee with a generic work method
class Employee:
    def work(self):
        print("The employee is working for the project")

# Step 2: Define Developer class inheriting from Employee and overriding the work method
class Developer(Employee):
    def work(self):
        print("The Developer works for project is technically")

# Step 3: Define Manager class inheriting from Employee and overriding the work method
class Manager(Employee):
    def work(self):
        print("The manager works for the project and handle manage the works for employees")

# Step 4: Create instances of Employee, Developer, and Manager
c1=Employee()
c2=Developer()
c3=Manager()

# Step 5: Call the work method on each instance to demonstrate polymorphism
c1.work()
c2.work()
c3.work()
        
# sample output
# The employee is working for the project
# The Developer works for project is technically
# The manager works for the project and handle manage the works for employees