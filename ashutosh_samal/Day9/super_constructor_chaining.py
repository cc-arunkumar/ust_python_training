#Super Constructor Chaining

#class employee creation
class Employee:
    def __init__(self,emp_id,name,dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
    
    #function to print details
    def get_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.dept}")

#class Developer inherited from Employee
class Developer(Employee):
    def __init__(self, emp_id, name, dept,platform):
        super().__init__(emp_id, name,dept)
        self.platform = platform

    def get_platform(self):
        print(f"Platform: {self.platform}")

#class FrontEnd inherited from Developer        
class FrontEnd(Developer):
    def __init__(self, emp_id, name, dept, platform):
        super().__init__(emp_id, name, dept, platform)

#class BackEnd inherited from Developer       
class BackEnd(Developer):
    def __init__(self, emp_id, name, dept, platform,):
        super().__init__(emp_id, name, dept, platform)

#object creation
d1 = Developer("D25","Niel","IT","MERN Stack")
f1 = FrontEnd("F10","Niten","FrontEnd","React")
b1 = BackEnd("B113","Mukesh","BackEnd","JAVA")

#list to store object
li = [d1,f1,b1]

#loop to iterate the list and calling the function
for i in li:
    i.get_details()
    i.get_platform()
    print("====================")
    
    
#Sample Execution
# Employee ID: D25
# Employee Name: Niel
# Employee Department: IT      
# Platform: MERN Stack
# ====================
# Employee ID: F10
# Employee Name: Niten
# Employee Department: FrontEnd
# Platform: React
# ====================
# Employee ID: B113
# Employee Name: Mukesh
# Employee Department: BackEnd
# Platform: JAVA
# ====================