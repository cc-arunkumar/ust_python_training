def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr.index(mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ("Not found")
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7  
result = binary_search(arr, target)
print(f"Element {target} found at index: {result}")
# Element 7 found at index: 1