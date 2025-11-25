# Insertion Sort Implementation
arr = [9, 8, 2, 7, 6]   # Initial unsorted list

# Outer loop: iterate through elements starting from index 1
for i in range(1, len(arr)):
    key = arr[i]        # Current element to insert in sorted part
    j = i - 1           # Index of last element in the sorted part
    
    # Shift elements of the sorted part that are greater than 'key'
    # Correct condition: arr[j] > key (not j > key)
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]   # Move element one position ahead
        j -= 1
    
    # Place 'key' at its correct position
    arr[j + 1] = key

# Print the sorted list
print("Sorted list (insertion sort):", arr)

# -------------------------
# Expected Output:
# Sorted list (insertion sort): [2, 6, 7, 8, 9]