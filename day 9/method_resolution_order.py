class Emp():
    def perform_task(self):
        print("Employee Working on generic tasks")


class Mgr(Emp):
    def perform_task(self):
        print("Manages the Project")


class Dev(Emp):
    # def perform_task(self):
        # print("Develops the Project")
    pass


class Tester(Emp):
    def perform_task(self):
        print("Testing the Project")

e1=Emp()
m1=Mgr()
d1=Dev()
t1=Tester()

employees=[e1,m1,d1,t1]
for emp in employees:
    emp.perform_task()
    

#Sample Output

# Working on generic tasks

# Manages the Project

# Working on generic tasks

# Testing the Project
