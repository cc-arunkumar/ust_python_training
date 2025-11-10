# Task 5: Combine Two Lists (Employee and Department)
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']

merge=list(map(lambda x,y:x+" works in "+y,names,depts))
print(merge)
# Sample output
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']