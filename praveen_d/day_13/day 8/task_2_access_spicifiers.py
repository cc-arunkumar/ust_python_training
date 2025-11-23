# public
# protected
# private

class Employee:
    def __init__(self):
        self.name="Jai"
        self._desigination="Developer"
        self.__salary=100000

    def show_employee_details_in_the_same_class(self):
        print(f"Name:{self.name}")
        print(f"Desigination:{self._desigination}")
        print(f"Salary:{self.__salary}")

emp1=Employee()

emp1.show_employee_details_in_the_same_class()
emp2=Employee()
print(emp2.name)
print(emp2._desigination)
print(emp2._Employee__salary)