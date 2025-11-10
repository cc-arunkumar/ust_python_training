# Task 4: Categorize Age Groups

# HR wants to classify employees as:

# “Junior” → if age < 30

# “Mid-level” → if 30 ≤ age < 45

# “Senior” → if age ≥ 45

# Use a lambda with conditional expressions

age=int(input("Enter Your Age: "))
ages=lambda age:"Junior" if age<30 else  "Mid-age" if age<45 else  "senior"
print(ages(age))

#sample output
# Enter Your Age: 25
# Junior