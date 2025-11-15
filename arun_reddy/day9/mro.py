class Employee:
    def perform_task(self):
        print("Employee Info...")
        print("Employee details...")
        print("=======================")
    

class Manager(Employee):
    pass

class Developer(Employee):
    def perform_task(self):
        print("Developer develops the code")
        print("Structures the code optimally")
        print("=======================")


class Tester(Employee):
    def perform_task(self):
        print("Tetsing findd the bugs...")
        print("Tester checkout the code...")
        print("=======================")

    
    
employee=Employee()
manager=Manager()
developer=Developer()
tester=Tester()
list1=[employee,manager,developer,tester]
for item in list1:
    item.perform_task()
     
     
     

# sample execution without removing the method in manager class 
# Employee Info...
# Employee details...
# =======================
# Maneger assigns the task
# Manager manages the task
# =======================
# Developer develops the code
# Structure steh code optimally
# =======================
# Tetsing findd the bugs...
# Tester checkout the code...

# sample execution  after removing the method in manager class 
# Employee Info...
# Employee details...
# =======================
# Employee Info...
# Employee details...
# =======================
# Developer develops the code
# Structures the code optimally
# =======================
# Tetsing findd the bugs...
# Tester checkout the code...
# =======================

