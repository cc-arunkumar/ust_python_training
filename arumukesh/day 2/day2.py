from functools import reduce 
list=[1,3,4,5,6]
res=reduce(lambda x,y:x+y,list)    
print(res)