#super constructor chaining
# creating the classes and making the constructor chaining so that code resuseablity should be done
#class employee
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def perform_task(self):
        print(f"{self.name} (ID: {self.emp_id}) works in {self.department} department.")

#class developer
class Developer(Employee):
    def __init__(self, name, emp_id, department, platform):
        super().__init__(name, emp_id, department)   # Call Employee constructor
        self.platform = platform

    def perform_task(self):
        print(f"{self.name} (ID: {self.emp_id}) develops on {self.platform} in {self.department} department.")

#class tester
class Tester(Employee):
    def __init__(self, name, emp_id, department, platform):
        super().__init__(name, emp_id, department)
        self.platform = platform

    def perform_task(self):
        print(f"{self.name} (ID: {self.emp_id}) tests code on {self.platform} in {self.department} department.")

#created list including my data
emp_list = [
    Employee("Bhargavi", 101, "HR"),
    Developer("Meena", 103, "Engineering", "Python"),
    Tester("VEena", 104, "QA", "Selenium")
]

#loop through the list
for e in emp_list:
    e.perform_task()
    
#output
# Bhargavi (ID: 101) works in HR department.
# Meena (ID: 103) develops on Python in Engineering department.
# VEena (ID: 104) tests code on Selenium in QA department.

