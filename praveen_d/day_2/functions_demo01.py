# sorting list using lambda function
# employee=[("pooja",35000),("Ravi",15000),("neha",50000)]

# employee.sort(key=lambda x :x[0])

# print(employee)
# ----------------------------------------------------------

#if else condition in lambda function

# check_employee_work_status= lambda hours :"overtime" if hours>8 else "Regular"

# print(check_employee_work_status(4))

# ----------------------------------------------------------
# using map in lambda

# salaries=[20,50,80,100,90,20]

# bonus=list(map(lambda sal:sal*0.05,salaries))

# print(bonus)

# using filter in lambda
# salaries=[20,50,80,100,90,20]

# bonus=list(filter(lambda sal:sal>50,salaries))
# print(bonus)
# ----------------------------------------------------------
from functools import reduce
sum_list=[1,2,3,4,5]

results= reduce(lambda a,b : a+b, sum_list)

print(results)