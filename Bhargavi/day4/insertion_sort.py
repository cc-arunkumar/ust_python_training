# Defined an insertion sort function that builds the sorted list one element at a time.
# Used a key variable to hold the current element being inserted.
# Shifted larger elements to the right until the correct position was found.
# Inserted the key into its correct position.
# Insertion Sort function

def insertion_sort(arr):
    # Loop through elements starting from index 1
    for i in range(1, len(arr)):
        key = arr[i]          # current element to insert
        j = i - 1             # index of previous element
        
        # Shift elements greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at its correct position
        arr[j + 1] = key


num = [33, 45, 78, 90, 11, 22, 33]

# Call insertion sort
insertion_sort(num)

# Print the sorted array
print("Sorted array:", num)

# Output:
# Sorted array: [11, 22, 33, 33, 45, 78, 90]
