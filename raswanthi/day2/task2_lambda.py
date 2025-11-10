#Lambda Task

#task 1
salary=50000
bonus=lambda sal:sal+(sal*0.10)
print(bonus(salary))

#output : 55000.0


#task2
l=[2,4,5,6,7,8]
result=list(filter(lambda x:x%2==0,l))
print(result)

#output: [2, 4, 6, 8]


#task3
employees=[
    ("Rahul",3),
    ("Priya",7),
    ("Karan",2),
    ("Divya",5)
]
employees.sort(key=lambda x:x[1])
print(employees)

#output: [('Karan', 2), ('Rahul', 3), ('Divya', 5), ('Priya', 7)]


#task4
age=35
answer=lambda age:"Junior" if age<30 else("Midlevel" if age<45 else "Senior")
print(answer(age))

#output: Midlevel


#task5
names = ['Arun', 'Neha', 'Vikram']
depts = ['HR', 'IT', 'Finance']

result = list(map(lambda x: f"{x[0]} works in {x[1]}", zip(names, depts)))
print(result)

#Output : ['Arun works in HR', 'Neha works in IT', 'Vikram works in Finance']