def quick_sort(list1):
    if len(list1)<=1:
        return list1
    
    pivot=list1.pop()
    left=[]
    right=[]

    for i in range(len(list1)):
        if list1[i]>pivot:
            right.append(list1[i])
        else:
            left.append(list1[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

list_1=[16,14,5,6,8]
print(quick_sort(list_1))