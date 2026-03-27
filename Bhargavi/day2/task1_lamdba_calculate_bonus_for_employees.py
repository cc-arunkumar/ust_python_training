# Task 1: Calculate Bonus for Employees

# Your team’s HR automation system needs to quickly calculate a 10% bonus for each employee based on their monthly salary.

# Requirement:
# Write a lambda function that takes a salary as input and returns the salary + 10% bonus.

# Example Input:
# salary = 50000

# Expected Output:
# 55000.0

# (Hint: bonus = salary * 0.10)

# Take salary input from user and convert it to integer
salary = int(input("Enter the salary: "))

# Define a lambda function to calculate bonus salary
# Formula: salary + (10% of salary)
bonus_salary = lambda salary: salary + (salary * 0.10)

# Print the calculated bonus salary
print("Bonus =", bonus_salary(salary))


# output:
# Enter the salary: 60000
# Bonus = 66000.0
