#Task : Quick Sort 

#Code
arr=[3,90,1,2,34,6]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in arr[1:]:
        if i<=pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)
sorted_array= quick_sort(arr)
print("Quick Sort : ",sorted_array)

#Output
# Quick Sort :  [1, 2, 3, 6, 34, 90]