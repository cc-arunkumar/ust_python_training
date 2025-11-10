def linear_sort(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [10, 23, 45, 70, 11, 15]  
target = 70
result = linear_sort(arr, target)
print(f"Element {target} found at index: {result}")
# Element 70 found at index: 3