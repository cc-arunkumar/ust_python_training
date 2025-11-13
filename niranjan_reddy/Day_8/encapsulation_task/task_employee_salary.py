# Encapsulation

# Create Employee class
class Employee:
    def __init__(self):
        self.name="Niranjan"
        self._designation="IT"
        self.__salary="75000"

    def  get_salary(self):
        print("Accessing salary using getter: ",self._Employee__salary)

    def set_salary(self,amount):
        if amount>0:
            self._Employee__salary=amount
            print("Updated Salary with given amount: ",self._Employee__salary)
        else:
            print("Please enter valid amount ")

    def show_info(self):
        print("Name:",self.name)
        print("Department:",self._designation)
        print("Salary:",self.__salary)


# Create emp1 object

emp1=Employee()
# emp1.set_salary(0)
# emp1.show_info()
# emp1.get_salary()
print("Name:",emp1.name)    
print("Department:",emp1._designation)
print("Trying to access private salary directly -> AttributeError: 'Employee' object has no attribute '__salary'.")
emp1.get_salary()

# Sample Output

# Name: Niranjan
# Department: IT
# Trying to access private salary directly -> AttributeError: 'Employee' object has no attribute '__salary'.
# Accessing salary using getter:  75000
