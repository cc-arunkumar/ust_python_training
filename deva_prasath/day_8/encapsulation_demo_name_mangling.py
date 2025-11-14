class Employee:
    def __init__(self):
        #public --> No Restrictions
        self.name="Dev"
        #protected --> Convention: should not be accessed outside the class or subclass
        self.__designation="Python Trainee"
        #private --> Name mangling : cannot be accesses directly outside the class
        self.__salary= 100000
        
        
    def show_employee(self):
        print("Name:",self.name)
        print("Designation:",self.__designation)
        print("Salary:",self.__salary)

emp1=Employee()
print("Name =",emp1.name)
# print("Designation =",emp1.__designation)   ---- # AttributeError: 'Employee' object has no attribute '__designation'
 
# print("Salary=",emp1.__salary)  -----AttributeError: 'Employee' object has no attribute '__salary'

print("Salary= ",emp1._Employee__salary)
print("Designation= ",emp1._Employee__designation)

#Name mangling --- _Classname__attribute


print(emp1.__dict__)

# {'name': 'Dev', '_Employee__designation': 'Python Trainee', '_Employee__salary': 100000}