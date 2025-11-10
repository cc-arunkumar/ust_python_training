#Binary search
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

numbers = [3,6,8,2,9,8]
x = 6
result = binary_search(numbers, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Element found at index 1
