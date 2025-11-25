# Quicksort Implementation (Recursive)
def quicksort(arr):
    # Base case: if list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose pivot (middle element here)
        key = arr[len(arr) // 2]
        
        # Partition the list into three parts:
        # left → elements smaller than pivot
        # mid  → elements equal to pivot
        # right → elements greater than pivot
        left = [x for x in arr if x < key]
        mid = [x for x in arr if x == key]
        right = [x for x in arr if x > key]
        
        # Recursively sort left and right, then combine
        return quicksort(left) + mid + quicksort(right)

# Sample unsorted list
list1 = [4, 8, 1, 3, 9, 7, 5]

# Call quicksort function
sort_list = quicksort(list1)

# Print the sorted list
print(f"Sorted list: {sort_list}")

# -------------------------
# Expected Output:
# Sorted list: [1, 3, 4, 5, 7, 8, 9]