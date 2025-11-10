# employees={
#     "pooja":25000,
#     "ravi":15000,
#     "arun":26000
# }
# employees=[("pooja",25000),("ravi",15000),("arun",26000)]
# employees.sort(key=lambda x:x[0])
# overtime_status=lambda hrs : "overtime" if hrs>8 else "regular"
# print(overtime_status(9))
# print(overtime_status(6))
salary=[40000,50000,60000]
# bonus = list(map(lambda sal:sal*0.05 , salary))
# print(bonus)
# bonus = list(filter(lambda sal: sal >50000 , salary))
# print(bonus)
from functools import reduce
bonus = reduce(lambda a,b: a+b,salary)
print(bonus)
