li=[3,2,1,4,5,3,2]

def quick_sort(list1):
    if len(list1)<=1:
        return list1
    pivot = list1[0]
    left = []
    right = []
    for i in list1[1:]:
        if pivot>i:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(li))

#Sample Output
#[1, 2, 2, 3, 3, 4, 5]