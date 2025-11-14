#MRO - Method Resolution Order

class Emp:
    def perform_task(self):
        print("Employee is working!!")

class Dev(Emp):
    def perform_task(self):
        print("Developer is working!!")

class Man(Emp):
    def perform_task(self):
        print("Manager is working!!")

class Test(Emp):
    pass

L=[Emp(),Dev(),Man(),Test()]

for i in L:
    i.perform_task()

#Output
# Employee is working!!
# Developer is working!!
# Manager is working!!
# Employee is working!!