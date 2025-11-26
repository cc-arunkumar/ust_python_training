tuple1=(1,2,3,4,5)
list=[]

for i in range(0,5):
    list.append(tuple1[i]*2)

tuple2=tuple(list)

print(tuple2)