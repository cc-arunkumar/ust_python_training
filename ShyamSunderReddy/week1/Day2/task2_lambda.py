# employees=[("Pooja",35000),("Shyam",90000),("Ram",10000)]
# employees.sort(key=lambda x:x[0])
# print(employees)

# overtime=lambda hours:"Overtime" if hours>8 else "regular"
# print(overtime(7))

# from functools import reduce
# salarie=[10000,20000,30000,40000,50000,60000]
# bonus=list(map(lambda sal:sal*0.05,salarie))
# new=list(filter(lambda sal: sal>30000,salarie))
# x=reduce(lambda a,b:a+b,salarie)
# print(bonus)
# print(new)
# print(x)

#Task 1: Calculate Bonus for Employees
bonus=lambda sal:sal+(sal*0.10)
print(bonus(5000))

#sample output
#5500.0

#Task 2: Identify Even Numbers in a List
nums=[101,102,103,104,105,106]
even=list(filter(lambda a:(a%2)==0,nums))
print(even)

#SAmple output
#[102, 104, 106]

#Task 3: Sort Employees by Experience
employees=[
    ("Rahul", 3),
    ("Priya", 7),
    ("Karan", 2),
    ("Divya", 5)
]
employees.sort(key=lambda x:x[1])
print(employees)

#Sample output
#[('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]

#Task 4: Categorize Age Groups
age=25
ans=lambda a:"Junior" if a<30 else "Mid-Level" if a<45 else"Senior"
print(ans(age))

#Sample output
#Junior

#Task 5: Combine Two Lists (Employee and Department)
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']
newemp=list(map(lambda x,y:f"{x}, works in ,{y}",names,depts))
print(newemp)

#Sample output
#['Arun, works in ,HR', 'Neha, works in ,IT', 'Vikram, works in ,Finance']