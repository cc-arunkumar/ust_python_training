# Task: Linear Search
# Scenario:
# Implement a linear search algorithm to find an element in a list.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # Return the index when the element is found
    return -1  # Return -1 if element not found

# Given list
numbers = [4, 2, 7, 1, 9, 3]
print("List:", numbers)

# User input
x = int(input("Enter number to search: "))
result = linear_search(numbers, x)

# Display result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


# Sample Output 1:
# List: [4, 2, 7, 1, 9, 3]
# Enter number to search: 6
# Element not found

# Sample Output 2:
# List: [4, 2, 7, 1, 9, 3]
# Enter number to search: 2
# Element found at index 1
