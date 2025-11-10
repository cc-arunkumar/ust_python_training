def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  


arr = [1, 3, 7, 15, 23, 34, 67] 
target = 23

result = binary_search(arr, target)
print("The number 23 is in the Index Number : ",result, "Of the Array ", arr) 

#Sample Output
# The number 23 is in the Index Number :  4 Of the Array  [1, 3, 7, 15, 23, 34, 67]