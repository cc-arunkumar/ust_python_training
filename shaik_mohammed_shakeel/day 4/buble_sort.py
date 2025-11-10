#bubble sort

list1=[8,4,2,7,1]
n=len(list1)

for i in range(n-1):
    is_swapped=False
    for j in range(n-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            is_swapped==True
        if(is_swapped==True):
            break
    
print("The Sorted List: ",list1)

#sample Output
# The Sorted List:  [1, 2, 4, 7, 8]


