# Initial list to be sorted
list1 = [4, 7, 3, 5, 1]

# Quick Sort function
# arr: the list to be sorted
# low: starting index of the sublist
# high: ending index of the sublist
def quick_sort(arr, low, high):
    # Base condition: only proceed if low < high
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # Recursively sort the sublist before the pivot
        quick_sort(arr, low, pivot_index - 1)
        # Recursively sort the sublist after the pivot
        quick_sort(arr, pivot_index + 1, high)

# Partition function
# This function rearranges the elements in such a way that
# all elements smaller than the pivot are on the left,
# and all elements greater than the pivot are on the right
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1        # Index of smaller element

    # Iterate over the sublist
    for j in range(low, high):
        # If current element is smaller than pivot
        if arr[j] < pivot:
            i = i + 1
            # Swap arr[i] with arr[j] to move smaller element to left
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot element with element at i+1
    # Now pivot is at its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1  # Return the pivot index

# Call quick_sort on the entire list
quick_sort(list1, 0, len(list1) - 1)

# Print the sorted list
print(list1)

# Sample output:
# [1, 3, 4, 5, 7]