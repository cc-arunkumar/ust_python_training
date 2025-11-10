# Task 5: Combine Two Lists (Employee and Department)
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']

merge=list(map(lambda names,depts: names+" works in "+depts,names,depts))
print(merge)





# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']