#Binary_search
# Function to perform binary search
def binary_search(a, search):
    left, right = 0, len(a) - 1  # Initialize the left and right pointers
    
    # Loop until the left pointer crosses the right pointer
    while left <= right:
        mid = left + (right - left) // 2  # Find the middle index

        # Check if the middle element is the search element
        if search == a[mid]:
            return mid  # Return the index if found
        
        # If the search element is greater, ignore the left half
        elif a[mid] < search:
            left = mid + 1
        
        # If the search element is smaller, ignore the right half
        else:
            right = mid - 1

    # Return -1 if the element is not found
    return -1

# Example array and search element
a = [50, 60, 100, 1, 4]

# Sort the array first (Binary Search works on sorted arrays)
a.sort()

search = 60

# Print the result of binary search
print(f"The search element is present at index: {binary_search(a, search)}")



#Sample output
# The search element is present in the index: 1

