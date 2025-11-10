
# Task 5: Combine Two Lists (Employee and Department)

# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.

names=["Arun","Neha","Vikram"]
depts=["HR","IT","Finance"]
merged_list=list(map(lambda a,b:a+ " works in "  +b,names,depts))
print(merged_list)

#sample output
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']