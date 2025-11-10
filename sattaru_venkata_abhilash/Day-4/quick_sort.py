# Task: Quick Sort
# Scenario:
# Implement the Quick Sort algorithm to sort a list of numbers in ascending order.

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    # Choose middle element as pivot
    mid = (low + high) // 2
    pivot = arr[mid]
    
    # Move pivot to the end for simplicity
    arr[mid], arr[high] = arr[high], arr[mid]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# Sample Output:
# Sorted array: [1, 5, 7, 8, 9, 10]
