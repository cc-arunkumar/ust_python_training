#  Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr) - 1): 
        is_swap = False
        for j in range(len(arr) - 1 - i): 
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                is_swap = True
        if not is_swap:
            break
    return arr



numbers = [64, 34, 25, 12, 22, 11, 90]
numbers = bubble_sort(numbers)
print("Sorted array is:", numbers)

# Sorted list is: [11, 12, 22, 25, 34, 64, 90]