# Combine Two Lists (Employee and Department)
# Task 5: Combine Two Lists (Employee and Department)
# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.
# Example Input:
# names = ['Arun', 'Neha', 'Vikram']
# depts = ['HR', 'IT', 'Finance']
# Expected Output:
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']

# List of employee names
names = ['Arun', 'Neha', 'Vikram']

# List of corresponding departments
depts = ['HR', 'IT', 'Finance']

# Use zip() to pair each name with its department
# Use map() with a lambda to format the string "Name works in Department"
combined = list(map(lambda n_d: f"{n_d[0]} works in {n_d[1]}", zip(names, depts)))

# Print the combined list
print(combined)

# Output:
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']