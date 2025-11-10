list1=[16,14,5,6,8]
for i in range(len(list1)-1):
    flag=0
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            flag=1
    if not flag:
        break
print(list1)