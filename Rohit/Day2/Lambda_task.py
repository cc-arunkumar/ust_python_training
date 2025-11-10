salaries = [40000,50000,60000,70000,80000]
bonus = list(map(lambda sal:sal +sal*0.1 , salaries))
print(salaries)


filterId = [12,7,8,75,43,22,68,49]
ans = list(filter (lambda id : id%2==0, filterId))
print(ans)



employees = [("Rahul ", 3), ("Priya",7), ("Karan", 2), ("Divya", 4)]
employees.sort(key=lambda x :x[1])
print(employees)


overtime_status = lambda age : "Junior-level" if age<30  else ( "mid-level" if age>30 or age<45 else "Senior-level")
print(overtime_status(36))



names = ['Arun', 'Neha','Vikram']
depts = ['HR', 'IT', 'FINANCE']


merged = list(map(lambda x: f"{x[0]} works in {x[1]}", zip(names, depts)))
print(merged)






