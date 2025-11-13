#employee management mini system


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary  # Monthly salary

    def calculate_yearly_salary(self):
        return self.salary * 12

    def increment(self):
        if self.department == "IT":
            bonus = self.salary * 0.10
        elif self.department == "HR":
            bonus = self.salary * 0.08
        elif self.department == "Finance":
            bonus = self.salary * 0.12
        else:
            bonus = self.salary * 0.05
        return bonus

    def show_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Department: {self.department}")
        print(f"Monthly Salary: Rs.{self.salary}")
        print(f"Yearly Salary: Rs.{self.calculate_yearly_salary()}")
        bonus = self.increment()
        print(f"Bonus Applied ({int((bonus/self.salary)*100)}%): Rs.{int(bonus)}")
        print("******************************")


# Create Employee objects
emp1 = Employee(101, "Arun Kumar", "IT", 75000)
emp2 = Employee(102, "Riya Sharma", "HR", 68000)
emp3 = Employee(103, "John Doe", "Finance", 80000)

# Display info
emp1.show_info()
emp2.show_info()
emp3.show_info()


#o/p:
# Employee ID: 101
# Employee Name: Arun Kumar
# Employee Department: IT
# Monthly Salary: Rs.75000
# Yearly Salary: Rs.900000
# Bonus Applied (10%): Rs.7500
# ******************************
# Employee ID: 102
# Employee Name: Riya Sharma
# Employee Department: HR
# Monthly Salary: Rs.68000
# Yearly Salary: Rs.816000
# Bonus Applied (8%): Rs.5440
# ******************************
# Employee ID: 103
# Employee Name: John Doe
# Employee Department: Finance
# Monthly Salary: Rs.80000
# Yearly Salary: Rs.960000
# Bonus Applied (12%): Rs.9600
# ******************************