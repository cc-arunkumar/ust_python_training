#Combine Two Lists (Employee and Department)

names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']
combined = list(map(lambda n_d: f"{n_d[0]} works in {n_d[1]}", zip(names, depts)))
print(combined)
#sample execution
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']
