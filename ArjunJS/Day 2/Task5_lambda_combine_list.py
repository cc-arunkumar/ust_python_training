#Task 5: Combine Two Lists (Employee and Department)
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']
output=list(map(lambda name,dept: name +" works in "+ dept,names,depts))
print(output)
#Output
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']