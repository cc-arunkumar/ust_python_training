# Task 5: Combine Two Lists (Employee and Department)

# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.

# Example Input:

# names = ['Arun', 'Neha', 'Vikram']
# depts = ['HR', 'IT', 'Finance']


# Expected Output:
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']



names = ['Arun', 'Neha', 'Vikram']

depts = ['HR', 'IT', 'Finance']

merge=list(map(lambda x,y:x+" works in "+y,names,depts))

print(merge)



# Sample output

# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']