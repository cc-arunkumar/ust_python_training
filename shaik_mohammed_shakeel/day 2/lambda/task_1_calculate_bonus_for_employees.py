
# Task 1: Calculate Bonus for Employees

# Your team’s HR automation system needs to quickly calculate a 10% bonus for each employee based on their monthly salary.

# Requirement:
# Write a lambda function that takes a salary as input and returns the salary + 10% bonus.

salary=[50000]
bonus=list(map(lambda sal:sal+(sal*0.1),salary))
print(bonus)


#sample output
#[55000.0]