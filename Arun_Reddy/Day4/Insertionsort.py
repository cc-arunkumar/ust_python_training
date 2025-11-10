list1=[3,12,9,6,5,1]
for i in range(len(list1)):
    j=i
    while j > 0 and list1[j]<list1[j-1]:
        list1[j],list1[j-1]=list1[j-1],list1[j]
        j=j-1

print(list1)

        
        
        
        



