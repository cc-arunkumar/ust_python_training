#linear search

# Define a function for linear search
def linear_search(arr, target):
    # Loop through each element in the array
    for i in range(len(arr)):
        # Check if the current element matches the target
        if arr[i] == target:
            return i   # Return the index if found
    # If target is not found in the array
    return "Not Found"

# Example list of numbers
nums = [10, 7, 8, 9, 1, 5]

# Search for 9 → should return its index
print("Index:", linear_search(nums, 9))

# Search for 2 → not in list, should return "Not Found"
print("Index:", linear_search(nums, 2))


#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/linear_search.py
# Index: 3
# Index: Not Found
# PS C:\Users\303379\day4_training> 

