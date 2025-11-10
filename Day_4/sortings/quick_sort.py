arr=[23,45,21,53,79,45]
start=0
end=len(arr)-1

print("Before sorting:", arr)
def quick_sort(arr,start,end):
    if start<end:
        partition_index=partition(arr,start,end)
        quick_sort(arr,start,partition_index-1)
        quick_sort(arr,partition_index+1,end)
    

def partition(arr,start,end):
    index=start-1
    pivot=arr[end]
    for j in range(start,end):
        if arr[j]<=pivot:
            index+=1
            arr[index],arr[j]=arr[j],arr[index]
    index+=1
    arr[index],arr[end]=arr[end],arr[index]
    
    return index

quick_sort(arr,start,end)
print("After sorting:",arr)

# Sample output
# Before sorting: [23, 45, 21, 53, 79, 45]
# After sorting: [21, 23, 45, 45, 53, 79]