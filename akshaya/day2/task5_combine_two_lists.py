#Task 5: Combine Two Lists (Employee and Department)
names=['Arun','Neha','Vikram']
depts=['HR','IT','Finance']
combined=list(map(lambda n, d: f"{n} works in {d}",names,depts))
print(combined)

#sample output
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']