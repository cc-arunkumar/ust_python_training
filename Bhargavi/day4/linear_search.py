# Linear Search function
# Defined a linear search function that checks each element one by one.
# Returns the index if the target is found, otherwise returns -1.
# Tested the function with a sample list and target 25.
# Since 25 is not in the list, the output is “Element not found”

def linear_search(arr, target):
    # Loop through each element in the list
    for i in range(len(arr)):
        # If current element matches target, return its index
        if arr[i] == target:
            return i
    # If target not found, return -1
    return -1

# Example list of numbers
num = [22, 45, 89, 23, 44, 77, 99]

# Target element to search
x = 25

# Call the linear search function
result = linear_search(num, x)

# Print result based on return value
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

#  Output:
# Element not found
