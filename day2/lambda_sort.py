from functools import reduce

employees =[("pooja",35000),("ravi",10000),("amit",20000)]
employees.sort(key=lambda x:x[0])
print(employees)

overtime_status = lambda hrs: "Overtime" if hrs > 8 else "regular"
print(overtime_status(6))

salaries = [40000,50000,60000,70000,80000]
bonus = list(map(lambda sal: sal*0.5,salaries))
print("salaries",bonus)

bonus = list(filter(lambda sal: sal>50000,salaries))
print("salaries",bonus)

list = [1,2,3,4,5,6]
results = reduce(lambda a,b : a+b,list)
print(results)