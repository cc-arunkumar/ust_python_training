# Task 1: Calculate Bonus for Employees

# Your team’s HR automation system needs to quickly calculate a 10% bonus for each employee based on their monthly salary.
# Requirement:
# Write a lambda function that takes a salary as input and returns the salary + 10% bonus.
# Example Input:
# salary = 50000
# Expected Output:
# 55000.0
# (Hint: bonus = salary * 0.10)

#code

# Take input from the user and convert it into an integer
salary = int(input("Enter your salary: "))

# Define a lambda function that calculates a 10% bonus
# The function takes 'salary' as input and returns salary + (10% of salary)
bonus = lambda salary: salary + (salary * 0.10)

# Call the lambda function with the given salary and print the result
print("Total salary after bonus:", bonus(salary))


#outPut
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task_lambda.py
# 50000
# 55000.0
# PS C:\Users\303379\day2_training> 



