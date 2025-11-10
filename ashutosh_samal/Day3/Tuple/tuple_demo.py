tuple1=(1,2,3,3,3,4,5)
list1=[]
for i in tuple1:
    list1.append(i*3)
print(list1)
print(tuple(list1))
print(4 in tuple1)
print(tuple1.count(3))
print(tuple1.index(3))

#Sample Execution
# [3, 6, 9, 9, 9, 12, 15]
# (3, 6, 9, 9, 9, 12, 15)
# True
# 3
# 2


tuple2 = (name,age,salary) = (("Neil",25,30000),("Nitin",27,40000),("Mukesh",29,35000))
print(tuple2)
#Sample Output
# (('Neil', 25, 30000), ('Nitin', 27, 40000), ('Mukesh', 29, 35000))


#Unpacking
for name,age,salary in tuple2:
    print("Name:",name)
    print("Age:",age)
    print("Salary:",salary)
    
#Sample Output
# Name: Neil
# Age: 25
# Salary: 30000
# Name: Nitin
# Age: 27
# Salary: 40000
# Name: Mukesh
# Age: 29
# Salary: 35000