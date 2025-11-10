#  Calculate Bonus for Employees

ans=int(input("Enter your salary"))
res=lambda sal: sal*0.10
print(res(ans)+ans)

#  Identify Even Numbers in a List
ids = [101, 102, 103, 104, 105, 106]
res1=list(filter(lambda x:x%2==0,ids))
print(res1)

#  Sort Employees by Experience0
employees = [
    ("Rahul", 3),
    ("Priya", 7),
    ("Karan", 2),
    ("Divya", 5)
]
employees.sort(key=lambda x:x[1])
print(employees)


#  Categorize Age Groups

age=int(input("Enter your age"))
res2=lambda x: "Junior"if x<30 else "Mid-level" if x<45 else "Senior"
print(res2(age))

#  Combine Two Lists (Employee and Department)

names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']

res3=list(map(lambda x,y: f"{x} works as {y}",names,depts))
print(res3)


# //samples Execution ///
# Enter your salary50000
# 55000.0
# [102, 104, 106]
# [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]
# Enter your age35
# Mid-level
# ['Arun works as HR', 'Neha works as IT', 'Vikram works as Finance']