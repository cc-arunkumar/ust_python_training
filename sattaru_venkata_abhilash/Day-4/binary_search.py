# Task: Binary Search
# Scenario:
# Implement a binary search algorithm to find an element in a sorted list.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index

        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            low = mid + 1   # Search in right half
        else:
            high = mid - 1  # Search in left half
    return -1  # Target not found


# Given list (must be sorted)
numbers = [1, 3, 5, 7, 9, 11, 13]
print("List:", numbers)

# User input
x = int(input("Enter number to search: "))
result = binary_search(numbers, x)

# Display result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


# Sample Output 1:
# List: [1, 3, 5, 7, 9, 11, 13]
# Enter number to search: 56
# Element not found

# Sample Output 2:
# List: [1, 3, 5, 7, 9, 11, 13]
# Enter number to search: 11
# Element found at index 5