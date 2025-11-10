# Task 1: Calculate Bonus for Employees
# Requirement:
# Write a lambda function that takes a salary as input and returns the salary + 10% bonus.

salary = int(input("Enter your salary: "))
calculate_bonus = lambda salary: salary + (salary * 0.10)
total = calculate_bonus(salary)
print(total)

# Sample Output:
# Enter your salary: 50000
# 55000.0
