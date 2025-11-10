from functools import reduce
employee=[("pooja",35000000),("ravi",172401)]
employee.sort(key=lambda x:x[0])
print(employee)

overtime_status= lambda hours:"overtime" if hours>8 else "regular"

print(overtime_status(6))

salaries = [40,50,60,70,80]
bonus = list(map(lambda sal:sal*0.5,salaries))
print(bonus)
bonus = list(filter(lambda sal:sal >50,salaries))
print(bonus)
results =  reduce(lambda a,b:a*b,salaries)
print(results)
