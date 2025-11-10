# tuple=(10,)
# print(tuple)
# print(type(tuple))

# tuple1=(10,20,25)
# print(tuple1)
# print(tuple1[0])
# print(tuple1[1:4])
#
# tuple2=(30,40,'a')
# print(tuple1+tuple2)
#
# list=list(tuple1)
# list.append(30)
# print(list)
#
# tuple2=tuple(list)
# print(tuple2)

# tuple1=(10,20,30)
# list=[]
# for i in tuple1:
#     list.append(i*5 )
# print(tuple(list))
#
# tuple1=(1,2,3,4,5)
# for i in tuple1:
#     if(i==3):
#         print("present")
#
# print(4 in tuple1)
#
# print(tuple1.count(3))
# print(tuple1.index(3))
# print(tuple1)

tuple1=(name, age, sal)=("harsh", 22, 50000)
print(tuple1)

for name,age,sal in tuple1:
    print(name,age,sal)