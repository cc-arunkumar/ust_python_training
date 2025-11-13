# Step 1: Define the Employee class with public, protected, and private attributes
class Employee:
    def __init__(self):
        self.name="manjunu"
        self._designation="Playboy"
        self.__salary=33000

    # Step 2: Method to display employee details from within the same class
    def show_employee_details_sameclass(self):
        print("name",self.name)
        print("Designation:",self._designation)
        print("salary:",self.__salary)

# Step 3: Create an instance of the Employee class
emp1=Employee()

# Step 4: Access public and protected attributes directly from outside the class
# print(emp1.__dict__)
print("Name=",emp1.name)
print("Designation:",emp1._designation)

# Step 5: Access private attribute using name mangling
print("salary:",emp1._Employee__salary)

# sample output
# Name= manjunu
# Designation: Playboy
# salary: 33000
        