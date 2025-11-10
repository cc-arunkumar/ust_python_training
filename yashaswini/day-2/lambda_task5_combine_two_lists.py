# Combine Two Lists (Employee and Department)


# You have two lists — one with employee names and another with their departments.
# Use a lambda to merge them into a single formatted string.


names=['Arun','Neha','Vikram']
depts=['HR','IT','Finance']
combined=list(map(lambda n:f"{n[0]} works in {n[1]}",zip(names,depts)))
print(combined)


#o/p:
#['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']