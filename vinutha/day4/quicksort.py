#Quick Sort

# Define the quicksort function
def quicksort(arr, low, high):
    # Continue only if the subarray has more than one element
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)   # Left side of pivot
        quicksort(arr, pi + 1, high)  # Right side of pivot

# Define the partition function
def partition(arr, low, high):
    # Choose the last element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    # Traverse through the array
    for j in range(low, high):
        # If current element is smaller or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap elements to place smaller ones before pivot
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return pivot index

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/quicksort.py
# Original array: [10, 7, 8, 9, 1, 5]
# Sorted array: [1, 5, 7, 8, 9, 10]
# PS C:\Users\303379\day4_training> 
