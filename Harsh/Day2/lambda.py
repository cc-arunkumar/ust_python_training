# emp=[("Pooja",35000),("Ravi",20000),("Amit",45000)]
# emp.sort(key=lambda x: x[0])
# print(emp)

# ovr_time= lambda hrs: "overtime" if hrs>8 else "regular"
# print(ovr_time(8))

# salr=[40,50,60,70,80]
# bonus=list(map(lambda sal : sal*0.5, salr))
# bonus1=list(filter(lambda sal : sal>60, salr))
# print(bonus)
# print(bonus1)

from functools import reduce
list=[1,2,3,4,5]
result=reduce(lambda x,y : x+y,list)
print(result)