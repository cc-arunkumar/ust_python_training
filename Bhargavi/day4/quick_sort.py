# Quick Sort implementation
# This program implements the Quick Sort algorithm, a divide-and-conquer sorting technique.
# It uses a partition function to place a pivot element in its correct position while rearranging smaller elements to the left and larger ones to the right.

# Partition function: places pivot element at correct position
def partition(arr, low, high):
    pivot = arr[high]        # choose last element as pivot
    i = low - 1              # index for smaller elements
    
    # loop through elements and rearrange based on pivot
    for j in range(low, high):
        if arr[j] <= pivot:  # if current element is smaller than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    
    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1             # return pivot index

# Quick Sort function: recursive sorting
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)   # partition index
        quick_sort(arr, low, pi - 1)     # sort left side
        quick_sort(arr, pi + 1, high)    # sort right side

# list
n = [100, 300, 400, 40, 56, 89]

# Call quick sort
quick_sort(n, 0, len(n) - 1)

# Print sorted array
print("Sorted array:", n)

# Output:
# Sorted array: [40, 56, 89, 100, 300, 400]
