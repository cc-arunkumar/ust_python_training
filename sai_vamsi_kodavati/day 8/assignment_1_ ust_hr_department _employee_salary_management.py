# assignment_1_ ust_hr_department _employee_salary_management

class Employee:
    def __init__(self):
        self.name = "Sai Vamsi"
        self._department = "IT"
        self.__salary = 30000

    def get_salary(self):
        return self.__salary

    def set_salary(self,amount):
        if amount > 0:
            self.__salary = amount
            print("Accessing salary using getter:",self.__salary)
        else:
            print("Invalid Amound:Amount is less than zero")

    def show_info(self):
        print("Name:",self.name)
        print("Department:",self._department)
        

emp1 = Employee()

emp1.show_info()

# print(emp1.__salary)
print("Trying to access private salary directly -> ERROR . AttributeError: 'Employee' object has no attribute '__salary")

emp1.set_salary(75000)

# ----------------------------------------------------------------------------------------------

# Sample Output

# Name: Sai Vamsi
# Department: IT
# Trying to access private salary directly -> ERROR . AttributeError: 'Employee' object has no attribute '__salary
# Accessing salary using getter: 75000









