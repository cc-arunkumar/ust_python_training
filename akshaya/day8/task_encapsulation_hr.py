# UST HR Department – Employee Salary
# Management
# Public attribute
# name
# Anyone in the company can see the employee's name.
# 2. Protected attribute
# _department
# Other teams should not directly change the employee’s department,
# but HR tools inside the system can access it.
# 3. Private attribute
# __salary
class Employee:
    def __init__(self, name, _department, __salary):
        self.name = name
        self._department = _department
        self.__salary = __salary  
        
#  get_salary()
# Returns the private salary (because outside cannot access it directly

    def get_salary(self):
        print("Salary:", self.__salary)
#  set_salary(amount)
# Allows updating salary only if amount is greater than zero
    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount

#  show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)
    def show_info(self):
        print(f"Name: {self.name} | Department: {self._department}")
        print("Salary:", self._Employee__salary)


emp1 = Employee("Ravi", "Finance", 50000)

print(emp1.__dict__)

print("Name =", emp1.name)
print("Department =", emp1._department)
# print("Salary =",emp1.__Salary)        [e.__salaryIt must FAIL (private attribute not accessible)].
print("Salary =", emp1._Employee__salary)  

# sample output
# print("Salary =",emp1.__Salary)
#                      ^^^^^^^^^^^^^
# AttributeError: 'Employee' object has no attribute '__Salary'.

# {'name': 'Ravi', '_department': 'Finance', '_Employee__salary': 50000}
# Name = Ravi
# Department = Finance
# Salary = 50000

