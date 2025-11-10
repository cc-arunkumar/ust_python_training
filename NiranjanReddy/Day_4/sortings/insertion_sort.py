list1=[5,3,6,2,9,1]
n=len(list1)
for i in range(n):
    temp=i
    while temp>0 and list1[temp-1]>list1[temp]:
        list1[temp-1],list1[temp]=list1[temp],list1[temp-1]
        temp-=1
print(list1)