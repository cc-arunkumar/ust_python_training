# Map_lambda
from functools import reduce
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']
results= list(map(lambda name,dept:f"{name} works in {dept}",names,depts))
print(results)

# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']