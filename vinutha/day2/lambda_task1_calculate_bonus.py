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

salary=int(input())
bonus=lambda salary:salary+(salary*0.10)
print(bonus(salary))

#outPut
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task_lambda.py
# 50000
# 55000.0
# PS C:\Users\303379\day2_training> 



