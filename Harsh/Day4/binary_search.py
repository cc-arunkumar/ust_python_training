def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

numbers = [1, 2, 3, 4, 7, 9]
target = 7
result = binary_search(numbers, target)
print("Binary Search Result at index:", result)

# Binary Search Result at index: 4