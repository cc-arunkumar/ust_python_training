def binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

arr = [2, 4, 6, 8, 10, 12]
target = 10
result = binary_search(arr, target, 0, len(arr) - 1)
print(f"Element found at index: {result}" if result != -1 else "Element not found")