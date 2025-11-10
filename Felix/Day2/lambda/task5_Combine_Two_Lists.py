from functools import reduce

names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']

result = list(map(lambda name,dept : name + " works in " + dept,names,depts))
print(result)

# output

# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']