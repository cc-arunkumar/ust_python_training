class Employee:
    def work(self):
         print("Works in the office")
class Developer(Employee):
     def work(self):
          print("Employee Works in the office")
class Manager(Employee):
      def work(self):
           print("Manager Works in the office")

e1=Employee()
e1.work()

e2=Developer()
e2.work()

e3=Manager()
e3.work()

# Smaple output:
# Works in the office
# Employee Works in the office
# Manager Works in the office