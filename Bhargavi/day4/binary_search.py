#Binary search
# # Binary search function
# Defined a binary search function with low, high, and mid pointers.
# Compared the target with the middle element and adjusted search boundaries.
# Returned the index if found, otherwise -1.
# Tested the function with a sample list and printed the result.

def binary_search(arr, target):
    low = 0                # starting index
    high = len(arr) - 1    # ending index
    
    # loop until search space is valid
    while low <= high:
        mid = (low + high) // 2   # middle index
        
        if arr[mid] == target:    # target found
            return mid
        elif arr[mid] < target:   # target is in right half
            low = mid + 1
        else:                     # target is in left half
            high = mid - 1
    
    return -1   # target not found


# Example list and target
numbers = [3, 6, 8, 2, 9, 8]  
x = 6                          

# Call the function
result = binary_search(numbers, x)

# Print result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")




# Element found at index 1
