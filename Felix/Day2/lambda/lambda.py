from functools import reduce

employee = [("Arun",55000),("Felix",25000),("Akhil",35000)]
employee.sort(key=lambda x:x[0],reverse=True)
print(employee)

overtime_status = lambda hours : "overtime" if hours>8 else "regular"
print(overtime_status(8))

employee = {("Arun",55000),("Felix",25000),("Akhil",35000)}
emp = sorted(employee,key=lambda x:x[1])
print(emp)


# map
salaries = [20,40,50,60]

bonous = list(map(lambda sal : sal*0.5,salaries))
print(bonous)

# filter

bonous = list(filter(lambda sal : sal>30,salaries))
print(bonous)

# reduce

l = [1,2,3,4,5]
result = reduce(lambda a,b : a+b,l)
print(result)
