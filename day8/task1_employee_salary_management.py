# Scenario: UST HR Department – Employee Salary Management
# UST wants a very small internal Python module that handles employee salary safely.
# The Class MUST include 3 methods:
# get_salary()
# Returns the private salary (because outside cannot access it directly)
# set_salary(amount)
# Allows updating salary only if amount is greater than zero
# show_info()
# Prints name + department
# But MUST NOT print salary directly (salary is private)
class Employee:
    def __init__(self, name, department, salary):
        self.name=name
        self._department=department
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount>0:
            self._salary=amount
        else:
            print("salary must be greater than zero")
            
    def show_info(self,):
        print("name: ",self.name)
        print("department: ",self._department)

# If someone tries:
# e.__salary
# It must FAIL (private attribute not accessible).

        
e = Employee("Arun", "IT", 50000)

# Show public + protected info
e.show_info()

# Instead of crashing, we simulate the failed access
print("Trying to access private salary directly -> ERROR")

# Update salary safely
e.set_salary(75000)

# Access salary using getter
print("Accessing salary using getter:", e.get_salary())



# Output
# name:  Arun
# department:  IT
# Trying to access private salary directly -> ERROR
# Accessing salary using getter: 50000

        