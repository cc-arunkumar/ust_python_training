#Combine Two Lists (Employee and Department)
names=eval(input("Enter the names: "))
depts=eval(input("Enter the departments: "))
comb=list(map(lambda n,d:f"{n} works in {d}",names,depts))
print(comb)
#Sample Execution:
# Enter the names: ["Raj","Rishi","Shivam"]
# Enter the departments: ["SDE","HR","MD"]
# ['Raj works in SDE', 'Rishi works in HR', 'Shivam works in MD']
