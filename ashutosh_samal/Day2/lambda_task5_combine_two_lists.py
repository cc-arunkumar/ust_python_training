#Task 5: Combine Two Lists (Employee and Department

names = ['Arun','Neha','Vikram']
dept = ['HR', 'IT', 'Finance']

merged = list(map(lambda x,y:f"{x} works in {y}",names,dept))
print(merged)

#Sample Execution
# ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']