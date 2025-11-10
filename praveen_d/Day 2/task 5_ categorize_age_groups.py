# Task 5_ Categorize Age Groups
# HR wants to classify employees as:

# “Junior” → if age < 30

# “Mid-level” → if 30 ≤ age < 45

# “Senior” → if age ≥ 45

# Use a lambda with conditional expressions.

# Example Input:
# age = 35


age = int (input("Enter the age:"))

catagory=lambda x : "Junior" if x<30 else "Mid-level" if x>=30 and x<45 else "Senior"

print(catagory(age))

# Sort Employees by Experience.py"
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
# PS C:\UST python> 

