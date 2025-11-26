# Task_2_Calculate_Bonus_for_Employees
# Objective:
# The HR team wants to calculate each employee’s efficiency score.
# They will provide two inputs:
# 1. Hours worked by the employee
# 2. Tasks completed by the employee
# The efficiency formula is:
# Efficiency = (tasks_completed / hours_worked) × 10
# Requirements:
# Create a function that accepts these two inputs as parameters.
# It should calculate the efficiency score using the above formula.
# It should return the calculated value to the main program.
# It should not print inside the function



salary=int(input("Enter the empoyee salary:"))

bouns =lambda sal: (sal*.10)+sal 
print(f"The bonus added salary is:{bouns(salary)}")

# Enter the empoyee salary:50000
# The bonus added salary is:55000.0