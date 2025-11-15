#Quick sort

# Quick Sort function to sort the array
def quick_sort(arr, left, right):
    if left < right:
        # Partition the array and get the pivot position
        partition_pos = partition(arr, left, right)
        
        # Recursively apply quick_sort to the left and right subarrays
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

# Partition function to find the pivot and reorder the array
def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]  # Set pivot as the last element
    
    # Loop to rearrange elements around the pivot
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1  # Move i to the right until arr[i] >= pivot
        while j > left and arr[j] >= pivot:
            j -= 1  # Move j to the left until arr[j] < pivot
        if i < j:
            # Swap elements if i < j
            arr[i], arr[j] = arr[j], arr[i]
    
    # Final swap to place the pivot in its correct position
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i  # Return the partition position of the pivot

# Array to be sorted
arr = [50, 60, 100, 1, 4]

# Call the quick_sort function to sort the array
quick_sort(arr, 0, len(arr) - 1)

# Print the sorted array
print("Sorted array: ", arr)


# Sample output
# Sorted array:  [1, 4, 50, 60, 100]






