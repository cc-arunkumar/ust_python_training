employees = [("pooja",35000),("Ravi",15000),("Amit",20000)]
employees.sort(key= lambda x:x[1])
print(employees)

overtime_status = lambda hours:"Overtime" if hours>8 else "Regular"
print(overtime_status(8))

salaries = [40,50,60,70,80]
bonus = list(map(lambda sal:sal*0.5, salaries))
print(bonus)

salaries = [40,50,60,70,80]
filt = list(filter(lambda sal : sal>50, salaries))
print(filt)

from functools import reduce
list=[1,2,3,4,5]
result = reduce(lambda a,b : a+b, list)
print(result)