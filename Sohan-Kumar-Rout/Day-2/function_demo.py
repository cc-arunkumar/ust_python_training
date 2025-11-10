#Args without return type

# def add_num(a,b):
#     print("Addition of two numbers are  : ")
#     sum=0
#     sum=a+b
#     print("Sum is : ",sum)

# add_num(20,20)

#Args with return type

# def square_num(a):
#     return a * a
# print(square_num(2))

#Without args with return



#Lambda function 

employee =[("Pooja",34000),("Ravi",1500),("Amit",20000)]
employee.sort(key = lambda x : x[1])
print("Sorted by Salary : ",employee)

employee =[("Pooja",34000),("Ravi",1500),("Amit",20000)]
employee.sort(key = lambda x : x[0])
print("Sorted by name : ",employee)

overtime_status = lambda hours : "Overtime" if hours>8 else regular
print("The person is working : ",overtime_status(9))

# map function
salaries =[40000,50000,60000,70000]
bonus = list(map(lambda sal : sal * 0.5, salaries))
print(bonus)

# Filter function
salaries =[40000,50000,60000,70000]
bonus = list(filter(lambda sal :  sal > 60000,salaries))
print(bonus)

#Reduce function
from functools import reduce
list= [1,2,3,4,5]
results = reduce(lambda a,b : a+b,list)
print("Sum in array :",results)


    

