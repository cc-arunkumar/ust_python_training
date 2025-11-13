class Employee:
    def __init__(self):
        self.id = "101"
        self._dep = "cyber"
        self.__sal = "25000"

    def show_employee_details_within_same_class(self):
        print(f"id :{self.id}")
        print(f"department :{self._dep}")
        print(f"salary :{self.__sal}")

emp1 = Employee()
emp1.show_employee_details_within_same_class()

# sample output:
# id :101
# department :cyber
# salary :25000
