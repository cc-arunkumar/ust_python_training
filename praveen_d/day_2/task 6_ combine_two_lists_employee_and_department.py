# Task 6_ Combine Two Lists (Employee and Department)
# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.
# Example Input:
# names = ['Arun', 'Neha', 'Vikram']
# depts = ['HR', 'IT', 'Finance']


names=['Arun','Neha','Vikram']
depts=['HR','IT','Finance']

joined_list=list(map(lambda name,dept: f"{name} works in {dept}",names,depts))

print(joined_list)

# Combine Two Lists (Employee and Department).py"
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']