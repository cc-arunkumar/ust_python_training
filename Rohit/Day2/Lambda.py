from functools import reduce

employees = [("pooja ", 35000), ("ravi",15000), ("Amit", 20000)]
employees.sort(key=lambda x :x[1])
print(employees)



overtime_status = lambda hours : "overtime" if hours>8  else "regular"

print(overtime_status(9))

salaries = [40000,50000,60000,70000,80000]
bonus = list(map(lambda sal:sal +sal*0.5 , salaries))
filterSalary= list(filter(lambda sal: sal>50000 , salaries))
print(bonus)
print(filterSalary)


values = [1,2,3,4,5]
result = reduce(lambda a, b: a + b, values)
print(result)