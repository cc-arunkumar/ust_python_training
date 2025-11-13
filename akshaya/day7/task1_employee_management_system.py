class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def show_info(self):
        print(f"Emp_id: {self.emp_id}\n Name: {self.name}\n Dept: {self.department}\n Sal: {self.salary}")

    def calculate_yearly_salary(self):
        yearly_salary = self.salary * 12
        print(f"Yearly salary for {self.name}: {yearly_salary}")
        

    def apply_bonus(self):
        if self.department == "IT":
            bonus = self.salary * 0.10
        elif self.department == "HR":
            bonus = self.salary * 0.08
        elif self.department == "Finance":
            bonus = self.salary * 0.12
        else:
            bonus = self.salary * 0.05
        print(f"Bonus for {self.name} ({self.department}): {bonus}")
        


# ---------------------- MAIN PROGRAM ----------------------

emp1 = Employee(101, "Damon", "IT", 75000)
emp2 = Employee(102, "Katherine", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Call methods correctly using the objects
emp1.show_info()
emp1.calculate_yearly_salary()
emp1.apply_bonus()

emp2.show_info()
emp2.calculate_yearly_salary()
emp2.apply_bonus()

emp3.show_info()
emp3.calculate_yearly_salary()
emp3.apply_bonus()
