
def bubble_sort(arr):
    
    for i in range(0,len(arr)-1):
        swap=False
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if not swap:
            break
            
    return arr

arr=[5,2,3,4,8,6,8,0,1,3]
print("Unsorted arr:", arr)
sorted=bubble_sort(arr)
print("sorted arr:", sorted)
            
# Unsorted arr: [5, 2, 3, 4, 8, 6, 8, 0, 1, 3]
# sorted arr: [2, 3, 4, 5, 6, 8, 0, 1, 3, 8]


    