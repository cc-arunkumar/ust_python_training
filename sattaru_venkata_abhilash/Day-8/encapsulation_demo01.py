class Employee:
    def __init__(self):
        # Public variable → can be accessed anywhere
        self.name = "Abhi"               

        # Protected variable → by convention should not be accessed outside class/subclass
        # Still accessible, but indicates "internal use"
        self._designation = "CEO"        

        # Private variable → name mangled by Python (converted to _Employee__salary)
        # Cannot be accessed directly as __salary
        self.__salary = 6000000000000000


    def show_employee(self):
        # Accessing variables inside class is allowed for all (public/protected/private)
        print("Name :", self.name)
        print("Designation:", self._designation)
        print("Salary:", self.__salary)



# ----------------------------
# Object creation
# ----------------------------
emp1 = Employee()

# Public variable → directly accessible
print("Name =", emp1.name)

# Protected variable → technically accessible, but not recommended
print("Designation =", emp1._designation)

# Private variable → must use NAME MANGLING to access
# Python internally renames __salary to _Employee__salary
print("Salary =", emp1._Employee__salary)


# sample output:
# Name = Abhi
# Designation = CEO
# Salary = 6000000000000000
