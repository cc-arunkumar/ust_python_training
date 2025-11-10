# Task 4: Categorize Age Groups

# HR wants to classify employees as:

# “Junior” → if age < 30

# “Mid-level” → if 30 ≤ age < 45

# “Senior” → if age ≥ 45

# Use a lambda with conditional expressions.
age=25



catez = lambda age: "junior" if age < 30 else "mid-level" if age < 45 else "senior"

print("categery:",catez(age))

# /sample output
# categery: junior
