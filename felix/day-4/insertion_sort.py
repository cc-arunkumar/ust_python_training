# insertion_sort

list1 = [4,3,5,7,8,34,56,90,76]
print(f"Initial arr: {list1}")

for i in range(1,len(list1)):
    temp = list1[i]
    j=i-1
    while j>=0:
        if temp<list1[j]:
            list1[j+1] = list1[j]
        else:
            list1[j+1] = temp
            break
        j-=1
    if j==-1:
        list1[0]=temp
            
    
print(f"Sorted array: {list1}")

# output

# Initial arr: [4, 3, 5, 7, 8, 34, 56, 90, 76]
# Sorted array: [3, 4, 5, 7, 8, 34, 56, 76, 90]