# Insertion sort
list1=[16,14,5,6,8]


for i in range(1,len(list1)):
    temp=list1[i]
    for j in range(i-1,-1,-1):
        if temp<list1[j]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        else: break

print(list1)

