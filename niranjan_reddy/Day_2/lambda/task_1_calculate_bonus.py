# Task 1: Calculate Bonus for Employees


# Your team’s HR automation system needs to quickly calculate a 10% bonus for each employee based on their monthly salary.

# Requirement:
# Write a lambda function that takes a salary as input and returns the salary + 10% bonus.

# Example Input:
# salary = 50000

# Expected Output:
# 55000.0

salary=int(input("Salary: "))

bonus=lambda salary:salary+(salary*0.10)

total=bonus(salary)

print(total)

# sample output

# Salary: 50000

# 55000.0
