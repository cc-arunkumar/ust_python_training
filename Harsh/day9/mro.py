class Emp:
    def __init__(self):
        pass
    def process_task(self):
        print("Processing task in Emp class")
class Manager(Emp):
    def process_task(self):
        print("Processing task in Manager class")
class Developer(Emp):
    # def process_task(self):
        pass
class Tester(Emp):
    def process_task(self):
        print("Processing task in Tester class")

employees = [Emp(),Manager(), Developer(), Tester()]
for emp in employees:
    emp.process_task()


# Processing task in Emp class
# Processing task in Manager class
# Processing task in Emp class
# Processing task in Tester class