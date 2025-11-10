def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            return mid
        
        elif(arr[mid] < target):
            low = mid + 1

        else:
            high = mid -1

    return -1

arr = [10,20,30,40,50,60,70]
target = 60
print("Number found at index:",binary_search(arr,target))

# ---------------------------------------------------------------------

# Sample Output
# Number found at index: 5