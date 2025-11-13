class Employee:
    def __init__(self):
        self.name="Harsh"
        self._designation="SDE-1"
        self.__salary=50000
        
    
e1=Employee()
print(f"Name :{e1.name},Designation:{e1._designation},Salary:{e1._Employee__salary}")


# Name :Harsh,Designation:SDE-1,Salary:50000