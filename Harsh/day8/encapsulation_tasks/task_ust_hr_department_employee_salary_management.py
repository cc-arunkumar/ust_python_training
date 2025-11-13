class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("ERROR: Salary must be greater than zero!")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")


e = Employee("Harsh", "IT", 50000)

print("Public attribute (name):", e.name)
print("Protected attribute (_department):", e._department)

try:
    print("Trying to access private salary directly:", e.__salary)
except :
    print("Trying to access private salary directly -> ERROR",AttributeError)

e.set_salary(75000)
print("Accessing salary using getter:", e.get_salary())
e.show_info()

# Public attribute (name): Harsh
# Protected attribute (_department): IT
# Trying to access private salary directly -> ERROR <class 'AttributeError'>
# Accessing salary using getter: 75000
# Name: Harsh
# Department: IT