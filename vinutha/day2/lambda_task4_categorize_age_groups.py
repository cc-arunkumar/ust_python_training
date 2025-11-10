# Task 4: Categorize Age Groups
# HR wants to classify employees as:
# “Junior” → if age < 30
# “Mid-level” → if 30 ≤ age < 45
# “Senior” → if age ≥ 45
# Use a lambda with conditional expressions.
# Example Input:
# age = 35
# Expected Output:
# "Mid-level"

#Code

classify_employee = lambda age: "Junior" if age < 30 else ("Mid-level" if age < 45 else "Senior")
age = int(input())
print(classify_employee(age))

#output
# PS C:\Users\303379\day2_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day2_training/task4_Categorize_Age_Groups.py
# 35
# Mid-level
# PS C:\Users\303379\day2_training> 

