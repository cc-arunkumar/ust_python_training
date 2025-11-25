# Function to perform recursive binary search
def binary_search(arr, target, left, right):
    # Base case: if left index exceeds right, element not found
    if left > right:
        return -1
    
    # Find the middle index
    mid = (left + right) // 2
    
    # Check if the middle element is the target
    if arr[mid] == target:
        return mid
    # If target is greater, search in the right half
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    # If target is smaller, search in the left half
    else:
        return binary_search(arr, target, left, mid - 1)

# Sample sorted array
arr = [2, 4, 6, 8, 10, 12]

# Target element to search
target = 10

# Call binary search function with full range (0 to len(arr)-1)
result = binary_search(arr, target, 0, len(arr) - 1)

# Print result: index if found, else "not found"
print(f"Element found at index: {result}" if result != -1 else "Element not found")

# -------------------------
# Expected Output:
# Element found at index: 4