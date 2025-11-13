# Step 1: Define the Employee class with public, protected, and private attributes
class Employee:
    def __init__(self):
        self.name="Vikash Reddy"
        self._department="It"
        self.__salary="30000"

    # Step 2: Getter method to access the private salary attribute
    def get_salary(self):
        return self.__salary

    # Step 3: Setter method to update salary with validation
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("Not allowed to update salary")

    # Step 4: Method to display employee information
    def show_info(self):
        print("Name:",self.name)
        print("Department:",self._department)

# Step 5: Create an Employee object, update salary, and display info
c1=Employee()
c1.set_salary(40000)
c1.show_info()

print("Trying to access private salary directly ->AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?")
print("Acessing a salary using getter:",c1._Employee__salary)

# sample output
# Name: Vikash Reddy
# Department: It
# Trying to access private salary directly ->AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?
# Acessing a salary using getter: 40000

