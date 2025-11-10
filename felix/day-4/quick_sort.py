# quick_sort

def partition(low,high,arr):
    pivot = arr[high]
    j = low-1
    for i in range(low,high):
        if arr[i]<pivot:
            j +=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[j+1],arr[high] = arr[high],arr[j+1]
    return j+1
            
    
    
    
def quicksort(low,high,arr):
    if low<high:
        ind = partition(low,high,arr)
        quicksort(low,ind-1,arr)
        quicksort(ind+1,high,arr)
    
arr = [2,1,4,5,3,6]
print(f"Initial array: {arr}")
quicksort(0,len(arr)-1,arr)
print(f"Sorted array: {arr}")
    
    
# output

# Initial array: [2, 1, 4, 5, 3, 6]
# Sorted array: [1, 2, 3, 4, 5, 6]