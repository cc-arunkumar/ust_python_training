# Task 5: Combine Two Lists (Employee and Department)
# Requirement:
# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.

names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']

merge = list(map(lambda x, y: x + " works in " + y, names, depts))
print(merge)

# Sample Output:
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']
