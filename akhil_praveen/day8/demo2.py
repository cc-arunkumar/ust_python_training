class Employee:
    def __init__(self):
        self.name = "Akhil"
        self._designation = "SDE - 1"
        self.__salary = 50000
        
emp1 = Employee()

# public data
print("Name: ",emp1.name)

# Protected data not recommended
print("Designation: ",emp1._designation)

# private data accessed through mangled name of variable
print("Salary : ",emp1._Employee__salary)
