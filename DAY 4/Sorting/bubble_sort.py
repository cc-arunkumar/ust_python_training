list1=[5,8,3,4,1]

for i in range(len(list1)-1):
    is_sorted=False
    for j in range(len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            is_sorted=True
    
    if(is_sorted==False): break

print(list1)    


"""
SAMPLE OUTPUT
[1, 3, 4, 5, 8]

"""