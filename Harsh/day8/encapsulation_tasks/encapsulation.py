# class Employee:
#     def __init__(self):
#         # Public attribute (can be accessed directly)
#         self.name = "Harsh"
        
#         # Protected attribute (convention: should not be accessed directly outside class/subclass)
#         self._designation = "SDE-1"
        
#         # Private attribute (name mangling: stored as _ClassName__attribute)
#         self.__salary = 50000


# # Create object
# e1 = Employee()

# # Accessing attributes
# print(f"Name :{e1.name}, Designation:{e1._designation}, Salary:{e1._Employee__salary}")

# # ------------------------------------------
# # Output:
# # Name :Harsh,Designation:SDE-1,Salary:50000


for i in range(1,6):
    for j in range(1,10):
        if (i+j>=6  and j-i<=4)  :
            # print(i+j,end="")
            print("*",end="")
        else:
            print("",end='')
    print()