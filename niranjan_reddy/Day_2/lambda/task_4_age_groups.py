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


age=int(input("age= "))

classify=lambda age:"Junior" if age<30 else "Mid-level" if age<45  else "Senior" 

print(classify(age))


# sample output

# age= 22

# Junior