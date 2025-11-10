from functools import reduce
# emp=[("Dev",5000),("Raj",2000)]
# emp.sort(key=lambda x:x[1])
# print(emp)

## for sorting by names just change the index to 0
# lambda arguments : expression


# overtime_status=lambda hours: "overtime" if hours>8 else "regular"
# print(overtime_status(7))

# salaries=[40000,50000,60000,70000,80000]
# bonus=list(map(lambda sal: sal*0.5, salaries))
# print(bonus)



# salaries=[40000,50000,60000,70000,80000]
# bonus=list(filter(lambda sal: sal>50000 ,salaries))
# print(bonus)

salaries=[1,2,3,4,5]
res=reduce(lambda a,b: a+b,salaries)
print(res)