#binary search 

# Define a function for binary search
def binary_search(arr, target):
    # Initialize the search boundaries
    low = 0
    high = len(arr) - 1

    # Continue searching while the range is valid
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2  

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid   # Return the index if found
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1 
        # If target is smaller, ignore the right half
        else:
            high = mid - 1 

    # If element is not found, return message
    return "Not Found"  

# Example list of sorted numbers
nums = [1, 5, 7, 8, 9, 10]

# Search for 9 → should return its index
print("Index:", binary_search(nums, 9))

# Search for 4 → not in list, should return "Not Found"
print("Index:", binary_search(nums, 4))

# #output
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/binary_search.py
# Index: 4
# Index: Not Found
# PS C:\Users\303379\day4_training> 
