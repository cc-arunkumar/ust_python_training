# bubble sort
list2=[8,5,0,6,1,2]
for i in range(len(list2)):
    for j in range(0,len(list2)-i-1):
        if list2[j]>list2[j+1]:
            list2[j],list2[j+1]=list2[j+1],list2[j]
            
print(list2)