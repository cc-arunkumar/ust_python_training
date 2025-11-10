# Task 4: Categorize Age Groups
# Requirement:
# HR wants to classify employees as:
# “Junior” → if age < 30
# “Mid-level” → if 30 ≤ age < 45
# “Senior” → if age ≥ 45
# Use a lambda function with conditional expressions.

categorize_age = lambda age: "Junior" if age < 30 else "Mid-level" if age < 45 else "Senior"

age_input = int(input("Enter employee age: "))
print(f"Employee category: {categorize_age(age_input)}")

# Sample Output:
# Enter employee age: 35
# Employee category: Mid-level
