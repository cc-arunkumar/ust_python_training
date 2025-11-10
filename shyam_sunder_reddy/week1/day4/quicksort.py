#Quick sort
def quicksort(arr):
    
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    left=[]
    right=[]
    for i in arr[1:]:
        if i>pivot:
            right.append(i)
        else :
            left.append(i)
    return quicksort(left)+[pivot]+quicksort(right)

    
    
arr=[40,20,10,30,50,80,60]
so=quicksort(arr)
print("Sorted array is: ",so)

# #Sample output
# Sorted array is:  [10, 20, 30, 40, 50, 60, 80]